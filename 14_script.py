from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
