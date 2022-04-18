from gettext import find
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int (x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html') 
    box = browser.find_element_by_id('treasure')
    x = box.get_attribute('valuex')
    y = calc(x)
    y_input = browser.find_element_by_id('answer')
    y_input.send_keys(y)
    check_rob = browser.find_element_by_id('robotCheckbox')
    check_rob.click()
    radio_rob = browser.find_element_by_id('robotsRule')
    radio_rob.click()
    submit_button = browser.find_element_by_class_name('btn-default')
    submit_button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

