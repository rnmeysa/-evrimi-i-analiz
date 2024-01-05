def su_kalitesi_hesapla(Ph, KOI, BOI, fosfat, sülfat, sıcaklık, amonyum, nitrat, nitrit, klor, renk, bulanıklık, sülfit, çözünmüş_oksijen, ec):
    sonuclar = ""


    if 6.5 <= Ph <= 8.5:
        sonuclar += "PH: İyi\n"
    else:
        sonuclar += "PH: Kötü\n"


    if KOI < 5:
        sonuclar += "KOI: İyi\n"
    else:
        sonuclar += "KOI: Kötü\n"

    if BOI < 3:
        sonuclar += "BOI: İyi\n"
    else:
        sonuclar += "BOI: Kötü\n"


    if fosfat < 1:
        sonuclar += "Fosfat: İyi\n"
    else:
        sonuclar += "Fosfat: Kötü\n"


    if sülfat < 250:
        sonuclar += "Sülfat: İyi\n"
    else:
        sonuclar += "Sülfat: Kötü\n"


    if sıcaklık >= 15 and sıcaklık <= 30:
        sonuclar += "Sıcaklık: İyi\n"
    else:
        sonuclar += "Sıcaklık: Kötü\n"



    return sonuclar


Ph = int(input("Su pH değerini girin: "))
KOI = float(input("KOI değerini girin: "))
BOI = float(input("BOI değerini girin: "))
fosfat = float(input("Fosfat değerini girin: "))
sülfat = float(input("Sülfat değerini girin: "))
sıcaklık = float(input("Sıcaklık değerini girin: "))

amonyum = float(input("Amonyum değerini girin: "))
nitrat = float(input("Nitrat değerini girin: "))
nitrit = float(input("Nitrit değerini girin: "))
klor = float(input("Klor değerini girin: "))
renk = float(input("Renk değerini girin: "))
bulanıklık = float(input("Bulanıklık değerini girin: "))
sülfit = float(input("Sülfit değerini girin: "))
çözünmüş_oksijen = float(input("Çözünmüş oksijen değerini girin: "))
ec = float(input("EC değerini girin: "))


print("\nSu Kalitesi Değerlendirmesi:")
print("-" * 30)
print(su_kalitesi_hesapla(Ph, KOI, BOI, fosfat, sülfat, sıcaklık, amonyum, nitrat, nitrit, klor, renk, bulanıklık, sülfit, çözünmüş_oksijen, ec))
