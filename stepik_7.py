from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')
    browser.get(link)

    getter1 = browser.find_element(By.ID, "num1")
    num1 = int(getter1.text)
    print(num1)
    getter2 = browser.find_element(By.ID, "num2")
    num2 = int(getter2.text)
    print(num2)
    summa = str(num1 + num2)
    print(summa)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summa)

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
