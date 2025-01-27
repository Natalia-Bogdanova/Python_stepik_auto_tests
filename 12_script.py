from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x и Посчитать математическую функцию от x  ln(abs(12*sin(x))).
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    # Проскроллить страницу вниз и Ввести ответ в текстовое поле.
    # button = browser.find_element(By.TAG_NAME, "button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

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
