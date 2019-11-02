from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Nikolay")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Romeiko")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Kyiv")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # do not forget to copy code for 30 sec
    time.sleep(30)
    # close browser after all operations
    browser.quit()

