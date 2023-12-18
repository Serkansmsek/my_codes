toplanacaksayilar = []
cikartilacaksayilar = []
carpilacaksayilar = []
boluneceksayilar = []
def toplama(sayilar):
    toplam=0
    for sayi in sayilar:
        toplam += sayi
    return toplam
def cikarma(sayilar):
    cikan=sayilar[0]
    for sayi in sayilar[1:]:
        cikan -= sayi
        return cikan
def carpma(sayilar):
    carpim = 1  # Çarpma işlemi için başlangıç değeri 1 olarak ayarlanır
    for sayi in sayilar:
        carpim *= sayi
    return carpim
def bolme(sayilar):
    bolum = sayilar[0]  # İlk sayıyı başlangıç değeri olarak alıyoruz
    for sayi in sayilar[1:]:  # Geri kalan sayıları böleceğiz
        if sayi != 0:  # Sıfıra bölme hatasını önlemek için kontrol ekliyoruz
            bolum /= sayi
        else:
            print("Hata: Sıfıra bölme hatası!")
            return None  # Sıfıra bölme hatasında None döndürüyoruz
    return bolum


print("lütfen yapmak istediğiniz işlemi giriniz\n1:Toplama\n2:Çıkarma\n3:Çarpma\n4:Bölme")
while True:
    islem=input("Yapılacak İşlemi Seçiniz Çıkmak için 'a' Basınız:")
    if islem.lower() == "a":
        break
    elif islem == "1":
        print("Toplama İşlemi Yapılıyor")
        while True:
            giris = input("Toplama işlemi için bir sayı girin. Eğer giriş yapmak istemiyorsanız 'q' basın: ")
            if giris.lower() == "q":
                print("Toplama İşlemi Hesaplanıyor...")
                break
            sayi = int(giris)
            toplanacaksayilar.append(sayi)

        sonuc = toplama(toplanacaksayilar)
        print("Toplama İşleminin Sonucu:", sonuc)
        toplanacaksayilar = []  # Listenin sıfırlanması

    elif islem == "2":
        print("Çıkarma İşlemi Yapılıyor")
        while True:
            giris = input("Çıkarma işlemi için bir sayı girin. Eğer giriş yapmak istemiyorsanız 'q' basın: ")
            if giris.lower() == "q":
                print("Çıkarma İşlemi Hesaplanıyor...")
                break
            sayi = int(giris)
            cikartilacaksayilar.append(sayi)

        sonuc = cikarma(cikartilacaksayilar)
        print("Çıkarma İşleminin Sonucu:", sonuc)
        cikartilacaksayilar = []  # Listenin sıfırlanması

    elif islem == "3":
        print("Çarpma İşlemi Yapılıyor")
        while True:
            giris = input("Çarpma işlemi için bir sayı girin. Eğer giriş yapmak istemiyorsanız 'q' basın: ")
            if giris.lower() == "q":
                print("Çarpma İşlemi Hesaplanıyor...")
                break
            sayi = int(giris)
            carpilacaksayilar.append(sayi)

        sonuc = carpma(carpilacaksayilar)
        print("Çarpma İşleminin Sonucu:", sonuc)
        carpilacaksayilar = []  # Listenin sıfırlanması

    elif islem == "4":
        print("Bölme İşlemi Yapılıyor")
        while True:
            giris = input("Bölme işlemi için bir sayı girin. Eğer giriş yapmak istemiyorsanız 'q' basın: ")
            if giris.lower() == "q":
                print("Bölme İşlemi Hesaplanıyor...")
                break
            sayi = int(giris)
            boluneceksayilar.append(sayi)

        sonuc = bolme(boluneceksayilar)
        if sonuc is not None:
            print("Bölme İşleminin Sonucu:", sonuc)
        boluneceksayilar = []  # Listenin sıfırlanması






