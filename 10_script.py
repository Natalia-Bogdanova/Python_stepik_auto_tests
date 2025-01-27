from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Извлечь первое число
    x = browser.find_element(By.CSS_SELECTOR, '#num1')
    # Извлечь текст и преобразовать в int в первом числе
    # x = int(x.text)
    # Извлечь первое число
    y = browser.find_element(By.CSS_SELECTOR,'#num2')
    #  # Извлечь текст и преобразовать в int во втором числе
    # y = int(y.text)
    # sumXY = x + y
    xy = str(int(x.text) + int(y.text))

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(xy)  # ищем элемент с текстом "Python"

    # Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
