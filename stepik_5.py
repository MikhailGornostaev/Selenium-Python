from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element(By.ID, "input_value")
    var_value = input1.text  # получим текст элемента между тегами
    calculated = calc(var_value)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(calculated)

    input3 = browser.find_element(By.ID, "robotCheckbox")
    input3.click()

    input4 = browser.find_element(By.ID, "robotsRule")
    input4.click()

    submit = browser.find_element(By.CLASS_NAME, "btn-default")
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
