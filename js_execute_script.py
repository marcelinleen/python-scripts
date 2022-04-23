from selenium import webdriver
import time
import math

# найти заданный X на странице, произвести вычисления, установить необходимые чек-боксы/радиобаттоны, чтобы кнопка Submit cтала доступна.
# из-за закрывающего футера обращаемся к js-скриптам

# функция для вычисления искомого значения
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html") # переход к браузеру
    x_element = browser.find_element_by_id("input_value") # поиск X
    x = x_element.text # считывание переменной
    answer = calc(x) # вычисление, обращение к функции
    input = browser.find_element_by_id("answer")
    input.send_keys(answer) # передача вычисления в инпут
    checkbox_rob = browser.find_element_by_id('robotCheckbox')
    checkbox_rob.click() # установка необходимого чек-бокса
    radiobutton_rob = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_rob) # скролл до нужного радиобаттона
    radiobutton_rob.click() # установка необходимого радиобаттона
    submit_but = browser.find_element_by_class_name('btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_but) # скролл до кнопки отправки формы
    submit_but.click() # отправка формы

finally:
    time.sleep(10) # оставляем вкладку открытой
    browser.quit() # закрываем браузер

# empty