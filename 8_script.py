from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # найти значение для переменной х
    x_element = browser.find_element(By.CSS_SELECTOR, 'label > .nowrap:nth-child(2)')
    x = x_element.text
    y = calc(x)
    # ввести ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    # Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    # Выбрать radiobutton "Robots rule!".
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()
    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
