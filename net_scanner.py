# paketleri oluşturmak, göndermek ve yakalamak için scapy kütüphanesini import ettim
import scapy.all as scapy
# kullanıcıdan ip adresi almak için optparse kütüphanesini kullanırım
import optparse


def ip_adresi():
    # burada parse objemi oluştururum
    parse_object = optparse.OptionParser()
    # burada kullanıcıdan almak istediğimiz kadar keyword arguments alırım
    # burada kullanıcı isterse -i veya --ipaddress ile taramak  istediğimiz ip adresini veririz
    # buradaki dest kısmında alınan girdiyi hangi veriye kaydetmek istediğimi belirtirim
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="Lütfen bir ip adresi giriniz")

    (girilen_ip_adresi, arguments) = parse_object.parse_args()
    # burada eğer kullanıcı ip adresi girmediyse ona bir hata mesajı gösteririm
    if not girilen_ip_adresi.ip_address:
        print("Lütfen bir ip adresi giriniz")

    return girilen_ip_adresi


# bu fonksiyonda cevap, istek ve yayın paketlerimi oluştururum
def ag_taramasi(ip):
    # burada ARP paketimi oluştururum (ARP= Address Resolution Protocol-> adres çözümleme protokolü)
    arp_istek_paketi = scapy.ARP(pdst=ip)
    # modeme bir yayın istedği göndermek için bir yayın paketi oluşturuyoruz
    yayin_paketi = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    birlesmis_paket = yayin_paketi / arp_istek_paketi
    (cevaplanalar, cevaplananlar) = scapy.srp(birlesmis_paket, timeout=1)
    cevaplananlar.summary()


kullanici_ip_adresi = ip_adresi()
ag_taramasi(kullanici_ip_adresi.ip_address)

