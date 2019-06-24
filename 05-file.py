from selenium import webdriver
browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

browser.find_element_by_css_selector('input[name="firstname"]').send_keys('q')
browser.find_element_by_css_selector('input[name="lastname"]').send_keys('q')
browser.find_element_by_css_selector('input[name="email"]').send_keys('q')

element = browser.find_element_by_id('file')

import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, '05-file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()