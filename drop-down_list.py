from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()  # open var link in Chrome browser
browser.get(link)

x = browser.find_element_by_id("num1")
y = browser.find_element_by_id("num2")
sum_xy = str(int(x.text) + int(y.text))  # sum of value num1 and num2 that are converted to data type integer
print(sum)


browser.find_element_by_xpath("//select[@id='dropdown']").click()
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum_xy)

btn = browser.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(30)  # add some time for copying the answer
browser.quit()


