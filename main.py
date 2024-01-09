from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import proxies
from user_actions import go_to_url

start_time = time.time()
working_proxy_count = 0
nonworking_proxy_count = 0
for proxy in proxies.list:
    options = Options()
    options.add_argument(f"--proxy-server={proxy}")
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(5)
    try:
        go_to_url(browser)
        print(proxy, " is working start to work")
        working_proxy_count += 1
        time.sleep(5)
    except Exception as e:
        working_proxy_count -= 1

elapsed_time = time.time() - start_time
print(f"Script execution time: {elapsed_time} seconds")
print(f"Working proxy count: {working_proxy_count}")
print(f"Nonworking proxy count: {nonworking_proxy_count}")
