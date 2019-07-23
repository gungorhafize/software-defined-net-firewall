from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr
import pox.lib.packet as pkt
from collections import namedtuple
import os
import csv

log = core.getLogger()
policyFile = "/pox/pox/misc/engellenenipler.csv"

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.info("Guvenlik duvari modulu etkinlestiriliyor)
        # firewall table
        self.firewall = {}

    def sendRule (self, src, dst, duration = 0):
        """
        Bu paketi düşürür ve bir süre benzerleri bırakmaya devam etmek için isteğe bağlı olarak bir akış kurar
        """
        if not isinstance(duration, tuple):
            duration = (duration,duration)
        msg = of.ofp_flow_mod()
	match = of.ofp_match(dl_type = 0x800,
			     nw_proto = pkt.ipv4.ICMP_PROTOCOL)
        match.nw_src = IPAddr(src)
        match.nw_dst = IPAddr(dst)
        msg.match = match
        msg.idle_timeout = duration[0]
        msg.hard_timeout = duration[1]
        msg.priority = 10
        self.connection.send(msg)

    # güvenlik duvarı kurallarinin firewall tableda olmasini sağlayan fonksiyon
    def AddRule (self, src=0, dst=0, value=True):
        if (src, dst) in self.firewall:
            log.info("Kural zaten mevcut drop: src %s - dst %s", src, dst)
        else:
            log.info("Yeni kural ekle drop: src %s - dst %s", src, dst)
            self.firewall[(src, dst)]=value
            self.sendRule(src, dst, 10000)

    # güvenlik duvarı kurallarının güvenlik duvarı tablosundan silinmesini sağlayan fonksiyon
    def DeleteRule (self, src=0, dst=0):
        try:
            del self.firewall[(src, dst)]
            sendRule(src, dst, 0)
            log.info("Kural silme drop: src %s - dst %s", src, dst)
        except KeyError:
            log.error("Kural bulunamadi drop: src %s - dst %s", src, dst)

    def _handle_ConnectionUp (self, event):
       
        self.connection = event.connection

        ifile  = open(policyFile, "rb")
        reader = csv.reader(ifile)
        rownum = 0
        for row in reader:
            # header row kaydet.
            if rownum == 0:
                header = row
            else:
                colnum = 0
                for col in row:
                    #print '%-8s: %s' % (header[colnum], col)
                    colnum += 1
                self.AddRule(row[1], row[2])
            rownum += 1
        ifile.close()

        log.info("Güvenlik duvarı kuralları yüklendi %s", dpidToStr(event.dpid))

def launch ():
    '''
    Guvenlik duvari modulu baslatiliyor...
    '''
    core.registerNew(Firewall)
