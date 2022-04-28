import pyperclip
import re
from selenium import webdriver
import time
import math

# get to link + click the button + switch the tab + solve a math task + put the solution and send the form

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) # math task

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html") # open the link
    first_button = browser.find_element_by_class_name('trollface') # find and click the first button
    first_button.click()
    new_tab = browser.window_handles[1] # find new tab
    browser.switch_to_window(new_tab) # switch to new tab
    x_element = browser.find_element_by_id('input_value') # find x
    x = x_element.text # read x.text
    answer = calc(x) # solve math task with x
    input = browser.find_element_by_id('answer')
    input.send_keys(answer) # write x
    submit = browser.find_element_by_class_name('btn-primary')
    submit.click() # send form
    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)
    pyperclip.copy(text)

finally:
    time.sleep(30) # give 10 sec before browser will close
    browser.quit() # exit browser

# empty