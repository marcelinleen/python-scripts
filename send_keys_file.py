from selenium import webdriver
import time
import os

# необходимо заполнить поля формы, загрузить файл и отправить форму

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html") # переход к браузеру
    inputs = browser.find_elements_by_class_name('form-control') # ищем все поля формы
    for input in inputs:
        input.send_keys("1") # заполняем все поля формы доступными значениями
    dir = "C:/Users/79507/environments/scripts/python-scripts/files/" # записываем директорию загружаемого файла
    file_name = "photo_2022-03-31_18-27-47.txt" # записываем имя загружаемого файла
    file_path = os.path.join(dir, file_name) # записываем полностью путь к загружаемому файлу
    input_file = browser.find_element_by_id('file') # ищем элемент для загрузки файла на странице
    input_file.send_keys(file_path) # загружаем файл
    submit = browser.find_element_by_class_name('btn-primary')
    submit.click() # ищем кнопку подтверждения отправки формы, отправляем

finally:
    time.sleep(10) # оставляем вкладку открытой
    browser.quit() # закрываем браузер

# empty