import csv


class Pizza:
    def __init__(self, ad, fiyat):
        self.__ad = ad
        self.__fiyat = fiyat

    def aciklama(self):
        return self.__ad

    def tutar(self):
        return self.__fiyat


class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita", 75.0)


class Klasik(Pizza):
    def __init__(self):
        super().__init__("Klasik", 100.0)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 125.0)


class Sade(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 75.0)


class Malzeme:
    def __init__(self, ad, fiyat):
        self.__ad = ad
        self.__fiyat = fiyat

    def aciklama(self):
        return self.__ad

    def tutar(self):
        return self.__fiyat


class Zeytin(Malzeme):
    def __init__(self):
        super().__init__("Zeytin ", 15.0)


class Mantar(Malzeme):
    def __init__(self):
        super().__init__("Mantar ", 20.0)


class KeciPeyniri(Malzeme):
    def __init__(self):
        super().__init__("Keçi Peyniri ", 25.0)


class Et(Malzeme):
    def __init__(self):
        super().__init__("Et ", 30.0)


class Sogan(Malzeme):
    def __init__(self):
        super().__init__("Soğan ", 35.0)


class Misir(Malzeme):
    def __init__(self):
        super().__init__("Mısır ", 25.0)


class Siparis:
    def __init__(self, pizza, malzeme):
        self.__pizza = pizza
        self.__malzeme = malzeme

    def getir_pizza(self):
        return self.__pizza

    def getir_malzeme(self):
        return self.__malzeme

    def getir_toplamtutar(self):
        return self.__pizza.tutar() + self.__malzeme.tutar()


def main():
    pizza_menu = [Klasik(), Margarita(), TurkPizza(), Sade()]
    malzeme_menu = [Zeytin(), Mantar(), KeciPeyniri(), Et(), Sogan(), Misir()]

    print("Menü:")
    for i, pizza in enumerate(pizza_menu):
        print(f"{i + 1}. {pizza.aciklama()} - {pizza.tutar()} TL")
    print("Malzemeler:")
    for i, malzeme in enumerate(malzeme_menu):
        print(f"{i + 1}. {malzeme.aciklama()} - {malzeme.tutar()} TL")

    pizza_secim = int(input("Lütfen bir pizza seçin (1-4): "))
    malzeme_secim = int(input("Lütfen bir malzeme seçin (1-6): "))

    pizza = pizza_menu[pizza_secim - 1]
    malzeme = malzeme_menu[malzeme_secim - 1]
    toplamtutar = pizza.tutar() + malzeme.tutar()
    print("Seçilen Pizza: ", pizza.aciklama())
    print("Seçilen Malzeme: ", malzeme.aciklama())
    print("Toplam tutar: ", toplamtutar)
    secim = input("Onaylıyor musunuz? e/h: ")
    if secim == 'e' or "E":


        ad = input("Adınız: ")
        while True:
            tc = input("TC Kimlik Numaranızı giriniz: ")
            if len(tc) != 11 or not tc.isdigit():
                print("Geçersiz TC Kimlik Numarası!")

            else:
                print("Geçerli TC Kimlik Numarası. İşleme devam ediliyor")
                break

        while True:
            kartno = input("Kredi Kartı Numaranız: ")
            if len(kartno) != 16 or not kartno.isdigit():
                print("Geçersiz Kart Numarası. Tekrar Giriniz")
            else:
                print("Geçerli Kart Numarası. İşleme devam edebilirsiniz.")
                break
        while True:
            cvv = input("Kredi Kartı CVV Kodunuz: ")
            if len(cvv) != 3 or not cvv.isdigit():
                print("Geçersiz CVV. Tekrar giriniz:")
            else:
                print("CVV Geçerli. İşleme devam edebilirsiniz.")
                break
        siparis_notu = input("Sipariş Notunuz: ")

        with open("Orders_Database.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([pizza.aciklama(), malzeme.aciklama(), toplamtutar, ad, tc, kartno, cvv, siparis_notu])

        with open("Orders_Database.csv", "r") as orders_file:
            orders_reader = csv.reader(orders_file)
            for row in orders_reader:
                print(row)
    else:
        print("İşleminiz iptal edildi")





if __name__ == "__main__":
    main()