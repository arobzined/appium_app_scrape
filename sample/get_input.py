class Input_():
    def __init__(self):
        self.marka = None
        self.model = None
        self.fiyat = None
        self.yil = None
        self.vites = None
        self.km = None
    def get_input(self):
        if (str(input("Marka seçmek istiyor musunuz?")).lower() == "evet"):
            self.marka = input("Lütfen markayı giriniz:")
            if (str(input("Model seçmek istiyor musunuz?")).lower() == "evet"):
                self.model = input("Lütfen modeli giriniz:")
        if (str(input("Fiyat Aralığınız var mı?")).lower() == "evet"):
            taban_fiyat = input("Taban fiyatı giriniz? (Yoksa boş bırakınız)")
            tavan_fiyat = input("Tavan fiyatı giriniz? (Yoksa boş bırakınız)")

            self.fiyat = [taban_fiyat,tavan_fiyat]
        if (str(input("Aracın üretim yılını belirlemek istiyor musunuz?")).lower() == "evet"):
            taban_yil = input("minimum yılı giriniz? (Yoksa boş bırakınız)")
            tavan_yil = input("maximum yılı giriniz? (Yoksa boş bırakınız)")

            self.yil = [taban_yil, tavan_yil]
        if (str(input("aracın vites tercihi önemli mi?")).lower() == "evet"):
            self.vites = input("Otomatik/Manuel?")
        if (str(input("Aracın kilometresini belirlemek istiyor musunuz?")).lower() == "evet"):
            taban_km = input("minimum km giriniz? (Yoksa boş bırakınız)")
            tavan_km = input("maximum km giriniz? (Yoksa boş bırakınız)")

            self.km = [taban_km, tavan_km]

        return {"marka":self.marka,
                "model":self.model,
                "fiyat":self.fiyat,
                "yil":self.yil,
                "vites":self.vites,
                "km":self.km}