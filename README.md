### Yazılım Tanımlı Ağ (Software Defined Network) Güvenlik Duvarı Projesi
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
