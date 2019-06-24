from selenium import webdriver

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)

treasure = browser.find_element_by_id('treasure')
x = treasure.get_attribute('valuex')

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

robotCheckbox = browser.find_element_by_id('robotCheckbox')
robotCheckbox.click()

robotsRule = browser.find_element_by_id('robotsRule')
robotsRule.click()

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()