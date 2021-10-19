from selenium import webdriver
from selenium.webdriver.common.by import By

import time

try:
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver_win32\chromedriver.exe')
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    # elements = browser.find_elements_by_tag_name_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()