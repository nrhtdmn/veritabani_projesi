from veritabani import Veritabani

# Veritabanı oluşturma
veritabanim = Veritabani("ornek.db")

# Tablo ekleme
veritabanim.tablo_olustur("kullanicilar", id="INTEGER PRIMARY KEY", isim="TEXT", yas="INTEGER")

# Tabloya veri ekleme
veritabanim.veriekle("kullanicilar", isim="Fatma", yas=30)

# Veritabanında arama
sonuclar = veritabanim.veritabaninda_ara("kullanicilar", "yas > 20")
for sonuc in sonuclar:
    print(sonuc)

# Veritabanında güncelleme
veritabanim.veritabani_guncelle("kullanicilar", "isim = 'Fatma'", yas=23)

# Veritabanında veri silme
veritabanim.veritabani_sil("kullanicilar", "isim = 'Ayşe'")


# Veritabanını kapatma
veritabanim.veritabani_kapat()

# veritabanim.veritabani_dosyasini_sil()
