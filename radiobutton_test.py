from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element_by_id('answer')
    y_element.send_keys(y)
    checkbox_rob = browser.find_element_by_id('robotCheckbox')
    checkbox_rob.click()
    radiobutton_rob = browser.find_element_by_id('robotsRule')
    radiobutton_rob.click()
    submit_but = browser.find_element_by_class_name('btn-default')
    submit_but.click()

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

