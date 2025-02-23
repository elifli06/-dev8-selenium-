from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def ödevim():
    try:
        # Chrome ayarlarını yapıyorum
        print("Chrome'u hazırlıyorum...")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        # WebDriver'ı başlatıyorum
        print("Tarayıcıyı açıyorum...")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # 1. Siteye gidiyorum
        print("Web sitesine gidiyorum...")
        driver.get("https://demoqa.com/webtables")
        time.sleep(2)

        # Geri kalan kodunuz aynı şekilde devam edecek...

        # 7. Kişiyi siliyorum
        print("Kişiyi listeden siliyorum...")
        delete_button = driver.find_element(By.XPATH, "//span[@title='Delete'][1]")
        delete_button.click()
        time.sleep(2)

        print("Aferin! Tüm işlemleri başarıyla tamamladın!")

    except Exception as e:
        print(f"Hata yaptın, dur! Hata mesajı: {e}")

    finally:
        print("Test tamamlandı, tarayıcıyı kapatıyorum. İyi çalışmalar!")
        driver.quit()

if __name__ == "__main__":
    ödevim()