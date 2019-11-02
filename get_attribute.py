from selenium import webdriver
import math

from selenium.webdriver.remote.webelement import WebElement

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)  # open link in Chrome browser


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


chest = browser.find_element_by_id("treasure")
mathvar = chest.get_attribute("valuex")
print(mathvar)
x = calc(mathvar)

input1 = browser.find_element_by_id("answer")
input1.send_keys(x)
checkbox1 = browser.find_element_by_xpath("//input[@id='robotCheckbox' and @required]")
checkbox1.click()
radiobtn1 = browser.find_element_by_xpath("//input[@id='robotsRule' and @value='robots']")
radiobtn1.click()

button1 = browser.find_element_by_css_selector("button.btn")
button1.click()
