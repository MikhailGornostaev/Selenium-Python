from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')
    browser.get(link)

    input_num = browser.find_element(By.ID, "input_value")
    num_x = input_num.text

    result = calc(num_x)

    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    browser.execute_script("window.scrollBy(0, 150);")

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)

    checkBox = browser.find_element(By.ID, "robotCheckbox")
    checkBox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
