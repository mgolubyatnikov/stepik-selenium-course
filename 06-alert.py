from selenium import webdriver
browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()

alert = browser.switch_to.alert
alert.accept()

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()