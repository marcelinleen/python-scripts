from selenium import webdriver
import time
import math

# get to link + click the button + access confirm + solve a math task + put the solution and send the form

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) # math task

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html") # open the link
    open_alert = browser.find_element_by_class_name('btn-primary') # find the button to get confirm window
    open_alert.click()
    confirm = browser.switch_to.alert # switch to confirm
    confirm.accept()
    x_element = browser.find_element_by_id('input_value') # find x
    x = x_element.text # read x.text
    answer = calc(x) # solve math task with x
    input = browser.find_element_by_id('answer')
    input.send_keys(answer) # write x
    submit = browser.find_element_by_class_name('btn-primary')
    submit.click() # send form
    

finally:
    time.sleep(10) # give 10 sec before browser will close
    browser.quit() # exit browser

# empty