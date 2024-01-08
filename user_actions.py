from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from random import choice

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

    try:
        if target_el.get_attribute("class") == dropdown_items_class:
            dropdown_btn_class = "group.cursor-pointer.relative.rounded-md"
            btn = browser.find_element(By.CLASS_NAME, dropdown_btn_class)
            btn.click()
            sleep(2)
        target_el.click()
        sleep(2)
        push_page_down_btn(browser.find_element(By.TAG_NAME, "body"))

    except WebDriverException as e:
        child_els = target_el.find_elements(By.CSS_SELECTOR, "*")

        if not len(child_els):
            [contact_us_actions(browser) for i in range(0, 2)]
        else:
            clicked_el = try_to_click_on_els(child_els)
            push_page_down_btn(clicked_el)

    sleep(50)


def try_to_click_on_els(els):
    for el in els:
        try:
            el.click()
            return el
        except Exception as e:
            print(el)
            continue
        finally:
            sleep(2)


def push_page_down_btn(body):
    range_limit = range(0, 4)
    limit = choice(range_limit)
    while limit:
        body.send_keys(Keys.PAGE_DOWN)
        sleep(2)
        if choice(range_limit) % 2 == 0:
            body.send_keys(Keys.PAGE_UP)
        limit -= 1
        sleep(5)


def contact_us_actions(browser):
    inputs = [
        get_el_by_tag(browser, "input"),
        get_el_by_tag(browser, "input"),
        get_el_by_tag(browser, "textarea"),
    ]

    random_input = choice(inputs)
    random_input.click()


def get_el_by_tag(browser, tag):
    return browser.find_element(By.TAG_NAME, tag)
