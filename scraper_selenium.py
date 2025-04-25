from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

# === Ayarlar ===
BASE_URL = "https://muhasebat.hmb.gov.tr/mali-istatistik-analiz-raporu"
DOWNLOAD_DIR = "veri/analiz_raporu"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# === Chrome başlatma ===
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

print("🚀 Tarayıcı başlatılıyor...")
driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=chrome_options)
driver.get(BASE_URL)
time.sleep(3)

# İndirme için session hazırlıyoruz
cookies = driver.get_cookies()
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

# Sayfada bulunan tüm linkleri tara
print("🔎 Sayfa içi bağlantılar taranıyor...")
links = driver.find_elements(By.TAG_NAME, "a")
found_any = False

for link in links:
    href = link.get_attribute("href")
    if href and any(ext in href.lower() for ext in [".pdf", ".xls", ".xlsx"]):
        filename = href.split("/")[-1].split("?")[0]
        filepath = os.path.join(DOWNLOAD_DIR, filename)

        if os.path.exists(filepath):
            print(f"✔️ Zaten var, indirilmiyor: {filename}")
            continue

        found_any = True
        print(f"📥 {filename} indiriliyor...")

        try:
            r = session.get(href, timeout=30)
            with open(filepath, "wb") as f:
                f.write(r.content)
            print(f"✅ {filename} başarıyla kaydedildi.")
        except Exception as e:
            print(f"❌ {filename} indirilemedi: {e}")

if not found_any:
    print("⚠️ Hiçbir uygun dosya bulunamadı.")

driver.quit()
print("🚪 Tarayıcı kapatıldı.")
