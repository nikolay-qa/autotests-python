from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

browser.get(link)

try:
    button1 = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']")
    button1.click()
    first_tab = browser.window_handles[0]
    second_tab = browser.window_handles[1]
    browser.switch_to.window(second_tab)

    x = int(browser.find_element_by_xpath("//span[@id='input_value']").text)
    answer_temp = str(math.log(abs(12*math.sin(x))))
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(answer_temp)
    button2 = browser.find_element_by_xpath("//button[@type='submit']")
    button2.click()

    alert = browser.switch_to.alert
    alert_text = alert.text

finally:
    print(alert_text)
    answer = alert_text.split()[-1]
    browser.quit()
