
# Türkiye Mali Rapor Scraper ve Yapay Zeka Destekli Analiz Sistemi

Bu proje, Türkiye Cumhuriyeti Hazine ve Maliye Bakanlığı'nın "https://muhasebat.hmb.gov.tr/mali-istatistik-analiz-raporu" adresinde yayınlanan mali analiz raporlarını otomatik olarak indirir, işler ve yapay zeka (GPT-4o) yardımıyla sade bir vatandaşın anlayabileceği şekilde yorumlar.(Yapay zeka kısmı daha sonra dahil edilecektir.)

---

## 🔧 Kullanılan Teknolojiler

- Python 3.x
- Selenium (Web tarayıcısı otomasyonu için)
- Requests (Dosya indirme)
- PDFPlumber (PDF içerik çıkartma)
- Pandas (Tablo işleme)
- OpenAI GPT-4o API (AI yorumlama)
- Flask (API sunucusu)
- ASP.NET MVC (Web arayüzü)

---

## 📁 Proje Yapısı

```
/veri/analiz_raporu/        # İndirilen PDF dosyaları
/vergi_scraper_selenium.py  # Selenium ile otomatik dosya indirme
/ai_api.py                  # Python AI yorumlayıcı servisi (Flask)
```

---

## 🚀 Kurulum

### Gerekli Paketler:
```bash
pip install selenium requests pdfplumber pandas openai flask
```

### ChromeDriver:
- `chromedriver.exe` dosyasını projenin kök klasörüne yerleştirin.
- Chrome tarayıcınızın versiyonuna uygun olmalıdır.

---

## 📥 PDF İndirme (vergi_scraper_selenium.py)

1. `mali-istatistik-analiz-raporu` sayfasına gider.
2. Sayfada bulunan tüm `.pdf`, `.xls`, `.xlsx` linklerini tarar.
3. Daha önce indirilmeyen dosyaları `veri/analiz_raporu/` klasörüne indirir.

---

## 📞 İletişim

Bu proje eğitim/analiz amacıyla oluşturulmuştur. Devlet verilerini şeffaf sunmak isteyen geliştiriciler içindir.
