from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first_name.send_keys("Vasya")

    first_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    first_name.send_keys("Poopkin")

    first_name = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    first_name.send_keys("vasily99@mail.ru")

    file_selector = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')
    file_selector.send_keys(file_path)

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
