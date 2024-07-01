import sqlite3
import os

class Veritabani:
    def __init__(self, veritabani_adi):
        self.veritabani_adi = veritabani_adi
        self.baglanti = None
        self.imlec = None
        self.baglan()

    def baglan(self):
        """Veritabanına bağlanır veya yeni bir veritabanı oluşturur."""
        if self.baglanti is None:
            self.baglanti = sqlite3.connect(self.veritabani_adi)
            self.imlec = self.baglanti.cursor()

    def tablo_olustur(self, tablo_adi, **kolonlar):
        """Yeni bir tablo oluşturur.
        Args:
            tablo_adi (str): Tablo adı.
            **kolonlar: Kolon adı ve veri tipi çiftleri.
        """
        self.baglan()
        kolon_tanimlari = ', '.join([f"{kolon} {tanim}" for kolon, tanim in kolonlar.items()])
        sorgu = f"CREATE TABLE IF NOT EXISTS {tablo_adi} ({kolon_tanimlari})"
        self.imlec.execute(sorgu)
        self.baglanti.commit()

    def veriekle(self, tablo_adi, **veriler):
        """Veritabanına veri ekler.
        Args:
            tablo_adi (str): Tablo adı.
            **veriler: Eklenmek istenen veriler.
        """
        self.baglan()
        kolonlar = ', '.join(veriler.keys())
        degerler = tuple(veriler.values())
        yerlestiriciler = ', '.join(['?'] * len(veriler))
        sorgu = f"INSERT INTO {tablo_adi} ({kolonlar}) VALUES ({yerlestiriciler})"
        self.imlec.execute(sorgu, degerler)
        self.baglanti.commit()

    def veritabani_guncelle(self, tablo_adi, kosul, **guncel_veriler):
        """Tabloda güncelleme yapar.
        Args:
            tablo_adi (str): Tablo adı.
            kosul (str): Güncelleme koşulu.
            **guncel_veriler: Güncellenmiş kolon-değer çiftleri.
        """
        self.baglan()
        kolon_degerleri = ', '.join([f"{kolon} = ?" for kolon in guncel_veriler.keys()])
        degerler = tuple(guncel_veriler.values())
        sorgu = f"UPDATE {tablo_adi} SET {kolon_degerleri} WHERE {kosul}"
        self.imlec.execute(sorgu, degerler)
        self.baglanti.commit()

    def veritabaninda_ara(self, tablo_adi, kosul="1=1"):
        """Veritabanında arama yapar.
        Args:
            tablo_adi (str): Tablo adı.
            kosul (str, optional): Arama koşulu. Defaults to "1=1".
        Returns:
            list: Arama sonuçları.
        """
        self.baglan()
        sorgu = f"SELECT * FROM {tablo_adi} WHERE {kosul}"
        self.imlec.execute(sorgu)
        return self.imlec.fetchall()

    def veritabani_sil(self, tablo_adi, kosul="1=1"):
        """Veritabanında veri siler.
        Args:
            tablo_adi (str): Tablo adı.
            kosul (str, optional): Silme koşulu. Defaults to "1=1".
        """
        self.baglan()
        sorgu = f"DELETE FROM {tablo_adi} WHERE {kosul}"
        self.imlec.execute(sorgu)
        self.baglanti.commit()

    def veritabani_kapat(self):
        """Veritabanı bağlantısını kapatır."""
        if self.baglanti:
            self.baglanti.close()
            self.baglanti = None
            self.imlec = None

    def veritabani_dosyasini_sil(self):
        """Veritabanı dosyasını siler."""
        self.veritabani_kapat()
        if os.path.exists(self.veritabani_adi):
            os.remove(self.veritabani_adi)
            print(f"{self.veritabani_adi} dosyası silindi.")
        else:
            print(f"{self.veritabani_adi} dosyası bulunamadı.")
