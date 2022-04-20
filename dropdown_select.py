import math
from webbrowser import get
from selenium import webdriver 
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains

# необходимо посчитать уравнение в заголовке и выбрать правильный ответ из dropdown

def calc(num1, num2):
    return str(int(num1) + int(num2)) # функция для вычисления


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html") # переход к браузеру
    # browser.get("http://suninjuly.github.io/selects2.html") # переход к браузеру с вторым вариантом dropdown (опционально)
    num1_element = browser.find_element_by_id("num1") # поиск элементов с значениями для вычисления
    num2_element = browser.find_element_by_id("num2")
    num1 = num1_element.text # считывание значений из переменных для вычисления
    num2 = num2_element.text
    value = calc(num1, num2) # вычисление в отдельной функции
    dropdown = Select(browser.find_element_by_id("dropdown")) # ищем dropdown на странице
    dropdown.select_by_visible_text(value) # ищем в dropdown нужное значение и выбираем его
    submit = browser.find_element_by_class_name("btn-default") # ищем кнопку submit
    submit.click() # кликаем на кнопку

finally:
    time.sleep(10) # оставляем вкладку открытой
    browser.quit() # закрываем браузер

# empty
