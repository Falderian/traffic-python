import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import proxies

for proxy in proxies.list:
    options = Options()
    options.add_argument(f"--proxy-server={proxy}")
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(5)
    try:
        browser.get("https://2ip.ru/")
        sleep(5)
    except Exception as e:
        (proxy, "is not working")
