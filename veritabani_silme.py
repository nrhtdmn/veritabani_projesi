from veritabani import Veritabani

# Mevcut veritabanına bağlanma veya yoksa oluşturma
veritabanim = Veritabani("ornek.db")

# Veritabanında bazı işlemler yapma
veritabanim.veriekle("kullanıcılar", isim="Mahmut", yas=33)

# Veritabanı dosyasını silme
veritabanim.veritabani_dosyasini_sil()
