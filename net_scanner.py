# paketleri olusturmak, gondermek ve yakalamak icin scapy kutuphanesini import ettim
import scapy.all as scapy
# kullanicidan ip adresi almak icin optparse kutuphanesini kullanirim
import optparse


def ip_adresi():
    # burada parse objemi olustururum
    parse_object = optparse.OptionParser()
    # burada kullanicidan almak istedigimiz kadar keyword arguments alirim
    # burada kullanici isterse -i veya --ipaddress ile taramak  istedigimiz ip adresini veririz
    # buradaki dest kisminda alinan girdiyi hangi veriye kaydetmek istedigimi belirtirim
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="Lutfen bir ip adresi giriniz")

    (girilen_ip_adresi, arguments) = parse_object.parse_args()
    # burada eger kullanici ip adresi girmediyse ona bir hata mesaji gosteririm
    if not girilen_ip_adresi.ip_address:
        print("Lutfen bir ip adresi giriniz")

    return girilen_ip_adresi


# bu fonksiyonda cevap, istek ve yayin paketlerimi olustururum
def ag_taramasi(ip):
    # burada ARP paketimi olustururum (ARP= Address Resolution Protocol-> adres cozumleme protokolu)
    arp_istek_paketi = scapy.ARP(pdst=ip)
    # modeme bir yayin istegi gondermek icin bir yayin paketi olusturuyoruz
    yayin_paketi = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    birlesmis_paket = yayin_paketi / arp_istek_paketi
    (cevaplananlar, cevaplanmayanlar) = scapy.srp(birlesmis_paket, timeout=1)
    cevaplananlar.summary()


kullanici_ip_adresi = ip_adresi()
ag_taramasi(kullanici_ip_adresi.ip_address)

