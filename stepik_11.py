from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')
    browser.get(link)

    first_window = browser.window_handles[0]

    troll_button = browser.find_element(By.CLASS_NAME, "trollface")
    troll_button.click()

    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    getter = browser.find_element(By.ID, "input_value")
    value = getter.text
    result = calc(value)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
