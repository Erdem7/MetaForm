import os

kitapListe = list ()

kitap = ["İnce memed","Yaşar Kemal"]

menu = """
{1} Kitap Ekle
{2} Kitap Çıkar
{3} Kitapları Listele
{0} Çıkış
"""

def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("ekleme işlemi yapıldı")
    print("Ana menüye dönmek için Enter'a basınız")
    input()

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True

    else:
        return False   

def kitapCikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap) #kitap çıkarılıyor 
        print("Kitap çıkarm işlemi yapıldı")
        print("Ana menüye dönmek için Enter'a basınız")
        input()
    else:
        print("Arattığınız kitap mevcut değildir !")
        print("Ana menüye dönmek için Enter'a basınız")
        input()
    
def listele(liste:list): 
    for i in liste: #listedekiler tuple olduğu için i ye çekiyoruz direk 
        print("Kitap adı : {}  ----- Yazar: {}".format(i[0],i[1]))  

    print("Ana menüye dönmek için Enter'a basınız")
    input()             

while True:
    os.system("cls")
    print(menu)
    
    secim = input("Seçiminiz Nedir ? ")

    if secim == "1":
        kitap_adi = input("Kitap adı giriniz :")
        kitap_yazar = input("Kitap'ın yazarını giriniz :")
        kitap = (kitap_adi,kitap_yazar)
        kitapEkle(kitap,kitapListe) # kitap ekleniyor


    elif secim == "2":
        kitap_adi = input("Kitap adı giriniz :")
        kitap_yazar = input("Kitap'ın yazarını giriniz :")
        kitap = (kitap_adi,kitap_yazar)
        kitapCikar(kitap,kitapListe)

    elif secim == "3":
        listele(kitapListe)

    elif secim == "q" and secim =="Q":
        print("Keyifli okumalar")
        quit()
    else:
        print("Hatalı seçim yaptınız")
