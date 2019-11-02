from selenium import webdriver
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()  # open var link in Chrome browser
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


chest = browser.find_element_by_xpath("//span[@id='input_value']")
math_var = calc(chest.text)

input1 = browser.find_element_by_id("answer")
input1.send_keys(math_var)
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
checkbox1 = browser.find_element_by_xpath("//input[@id='robotCheckbox' and @required]")
checkbox1.click()
radiobtn1 = browser.find_element_by_xpath("//input[@id='robotsRule' and @value='robots']")
radiobtn1.click()

btn = browser.find_element_by_xpath("//button[@type='submit']")
btn.click()


time.sleep(10)  # add some time for copying the answer
browser.quit()



