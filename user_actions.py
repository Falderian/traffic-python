from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from time import sleep
from random import choice, randint

base_url = "https://tiny-chough.cloudvent.net/"
passw = "rhjyjy?cjanm!"


def go_to_url(browser):
    browser.get(base_url)
    pass_input = browser.find_element(By.ID, "password")
    pass_input.send_keys(passw)
    pass_input.send_keys(Keys.ENTER)

    dropdown_items_class = "block text-danger text-lg px-4 py-2 md:hover:bg-violet-50 md:hover:rounded-b-md"

    all_links = browser.find_elements(By.TAG_NAME, "a")
    target_el = choice(all_links)
    browser.execute_script("arguments[0].scrollIntoView();", target_el)
    contact_us_actions(browser)
    sleep(random())
    try:
        if target_el.get_attribute("class") == dropdown_items_class:
            dropdown_btn_class = "group.cursor-pointer.relative.rounded-md"
            btn = browser.find_element(By.CLASS_NAME, dropdown_btn_class)
            btn.click()
            sleep(random())
        sleep(random())
        browser.execute_script("arguments[0].click();", target_el)
        push_page_down_btn() if random() % 2 == 0 else contact_us_actions(browser)

    except WebDriverException as e:
        print(e)

    sleep(random())


def push_page_down_btn(browser):
    body = browser.find_element(By.TAG_NAME, "body")
    range_limit = range(0, 5)
    limit = choice(range_limit)
    while limit:
        body.send_keys(Keys.PAGE_DOWN)
        sleep(random())
        if choice(range_limit) % 2 == 0:
            body.send_keys(Keys.PAGE_UP)
        limit -= 1
        sleep(random())


def contact_us_actions(browser):
    inputs = [
        *browser.find_elements(By.XPATH, "//input"),
        browser.find_element(By.XPATH, "//textarea"),
    ]

    random_input = choice(inputs)
    browser.execute_script("arguments[0].click();", random_input)


def random():
    return randint(0, 10)
