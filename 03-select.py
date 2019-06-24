from selenium import webdriver

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/selects1.html'
browser.get(link)

num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text

result = int(num1) + int(num2)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(result))

submit = browser.find_element_by_css_selector('button[type="submit"]')
submit.click()