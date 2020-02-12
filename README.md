### Yazılım Tanımlı Ağ Güvenlik Duvarı Projesi (Software Defined Network) 
---
##### Kullanılan Ana Araçlar ve Teknolojiler:
- SDN Controller
- Mininet for network simulation
- Pox Controller
- Virtual Box
- Coding in Python 
- Opendaylight

Belirli kaynak ve hedef IP adreslerine sahip paketleri bırakmak için denetleyiciye kurallar eklendi.
IP adres çiftleri CSV dosya formatında saklanmıştır ve bu çiftler Python'da pox tarafından okunur ve işlenir.
Güvenlik duvarı IP çifti listesini giriş olarak alır ve ağdaki switclere yükler.
Switch ve hoslari barındıran ağ topolojisi mininet'te olusturuldu.
Bu projenin amacı IP adreslerini engellemektir.

Bu projenin birincil işlevi, POX denetleyicisine hangi IP adreslerinin engellenmesi gerektiğini belirten bir güvenlik duvarı eklemektir. Mininet yüklü sanal makinede küçük bir ağ kurulumu yaptik ve bu ağ, her biri bir ana bilgisayara (host) sahip 6 anahtar (switch) içermektedir. Güvenlik duvarı algoritması, tüm IP adreslerinin engellenmesi gerektiğini belirten güvenlik duvarı politikalarına uygun çalışan POX denetleyicisi ile birlikte başlatılır. Böylece, bir IP adresi adresinden anahtar bir paket aldığında,güvenlik duvarı modülüne uyacak ve engellenecek paketler için switche bir 'drop' bastıracak olan POX'a gönderilir. Bu nedenle, switch bu kaynaktan gelen diğer paketleri engelleyecektir. IP adresinden gelen paketlerin geri kalanı yalnızca paketleri POX kontrol cihazlarına göndermeye gerek kalmadan switchler tarafından yönetilir, böylelikle de yazılım tanımlı ağ ilkelerine uyulmus olur.

---
```sh
cd mininet/custom
cp engellenenipler.csv firewall.py pox/pox/misc
sudo mn –custom topology.py –topo mytopo –mac –controller=remote, ip, port=6633.
```
---
##### 🌐Ağ Topolojisi🌐
---
![nettopo](https://user-images.githubusercontent.com/33956266/61745808-0106ad00-ada3-11e9-946c-dcaecfe12aad.JPG)

