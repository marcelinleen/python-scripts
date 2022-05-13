import pyperclip
import re
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# get to link + wait until price change to 100$ + click "Book" + solve the math task + send the answer

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) # math task

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html") # open the link
    price = WebDriverWait(browser, 12).until (EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element_by_id("book")
    button.click()
    x_element = browser.find_element_by_id('input_value') # find x
    x = x_element.text # read x.text
    answer = calc(x) # solve math task with x
    input = browser.find_element_by_id('answer')
    input.send_keys(answer) # write x
    submit = browser.find_element_by_id('solve')
    submit.click() # send form
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
    text = "".join(text)
    pyperclip.copy(text)
    # browser.execute_script("window.open('https://stepik.org/course/575/promo?auth=login');")
    # time.sleep(10)
    # email_input = browser.find_element_by_xpath('/input[type="email"]')
    # email_input.send_keys('kryugersha@gmail.com')
    # password_input = browser.find_element_by_id('id_login_password')
    # password_input.send_keys('krgrsha3755')
    # login_button = browser.find_element_by_class_name('sign-form__btn')
    # login_button.click()


finally:
    time.sleep(10) # give 10 sec before browser will close
    browser.quit() # exit browser

#empty