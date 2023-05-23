#paketleri olusturmak, gondermek ve yakalamak icin scapy kutuphanesini import ettim
import scapy.all as scapy
#kullanicidan ip adresi ve dosya adi almak icin optparse kutuphanesini kullandim
import optparse


def ip_adresi():
    #burada bir parse objesi olustururum
    parse_object = optparse.OptionParser()
    # burada kullanicidan almak istedigimiz kadar keyword arguments alirim
    # burada kullanici isterse -i veya --ipaddress ile taramak  istedigimiz ip adresini veririz
    # buradaki dest kisminda alinan girdiyi hangi veriye kaydetmek istedigimi belirtirim
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="Lutfen bir ip adresi giriniz")
    parse_object.add_option("-w", "--write", dest="dosya_adi", help="Kaydedilecek dosyanin adini belirtin")
    (girilen_ip_adresi, arguments) = parse_object.parse_args()

    if not girilen_ip_adresi.ip_address:
        print("Lutfen bir ip adresi giriniz")

    return girilen_ip_adresi

#bu fonksiyonda cevap, istek ve yayin paketlerimi olustururum
def ag_taramasi(ip, dosya_adi=None):
    arp_istek_paketi = scapy.ARP(pdst=ip)
    #modeme bir yayin istegi gondermek icin bir yayin paketi olusturdum
    yayin_paketi = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    birlesmis_paket = yayin_paketi / arp_istek_paketi
    cevaplananlar, cevaplanmayanlar = scapy.srp(birlesmis_paket, timeout=1)
    #buradaki summary metodu bir paketin onemli bilgilerini ozet seklinde bize sunar
    cevaplananlar.summary()

#buradaki if kosulunda eger kullanici dosya adi verip kaydetmek istediyse sonuclari bir txt dosyasina kaydeder
    if dosya_adi:
        with open(dosya_adi, 'w') as dosya:
            for cevap in cevaplananlar:
                dosya.write(cevap[1].summary() + "\n")
        print("Sonuclar", dosya_adi, "dosyasina kaydedildi.")


kullanici_ip_adresi = ip_adresi()
ag_taramasi(kullanici_ip_adresi.ip_address, kullanici_ip_adresi.dosya_adi)
