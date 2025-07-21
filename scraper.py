# -*- coding: utf-8 -*-
import sys
import urllib3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.stdout.reconfigure(encoding='utf-8')

def init_driver_and_load_page(ean):
    try:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(f"https://www.barcodelookup.com/{ean}")
        return driver
    except Exception as e:
        print(f"[!] Erreur ouverture page BarcodeLookup : {e}", file=sys.stderr)
        return None

def scrape_barcode_lookup(ean):
    driver = init_driver_and_load_page(ean)
    if not driver:
        return {"title": "", "image_url": ""}

    try:
        wait = WebDriverWait(driver, 10)
        try:
            nom_produit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h4"))).text.strip()
        except:
            nom_produit = ""

        try:
            image_url = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#largeProductImage img"))).get_attribute("src")
        except:
            image_url = ""

        driver.quit()
        return {"title": nom_produit, "image_url": image_url}

    except Exception as e:
        print(f"[!] Erreur scraping titre/image : {e}", file=sys.stderr)
        driver.quit()
        return {"title": "", "image_url": ""}
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("EAN manquant.")
        sys.exit(1)

    ean = sys.argv[1].strip()
    result = scrape_barcode_lookup(ean)
    print(result)
