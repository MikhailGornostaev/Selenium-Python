from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')
    browser.get(link)

    # getter_p = browser.find_element(By.ID, "price")
    # price = getter_p.text
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    book = browser.find_element(By.ID, "book")
    book.click()

    getter = browser.find_element(By.ID, "input_value")
    value = getter.text
    result = calc(value)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)

    submit = browser.find_element(By.ID, "solve")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
