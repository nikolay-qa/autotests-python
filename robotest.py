from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)  # open link in Chrome browser


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


mathvar = browser.find_element_by_id("input_value")
x = calc(mathvar.text)

input1 = browser.find_element_by_id("answer")
input1.send_keys(x)
checkbox1 = browser.find_element_by_xpath("//input[@id='robotCheckbox' and @required]")
checkbox1.click()
radiobtn1 = browser.find_element_by_xpath("//input[@id='robotsRule' and @value='robots']")
radiobtn1.click()

button1 = browser.find_element_by_css_selector("button.btn")
button1.click()
