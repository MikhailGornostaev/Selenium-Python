from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    value = browser.find_element(By.ID, "input_value")
    x_val = value.text
    result = calc(x_val)
    print(result)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
