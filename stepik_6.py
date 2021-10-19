from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')
    browser.get(link)

    getter = browser.find_element(By.ID, "treasure")
    x_val = getter.get_attribute("valuex")
    x_res = calc(x_val)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(x_res)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
