from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Natali")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Bogdanova")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ya.n-bog@ya.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '15товаров в заказе.json')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
