from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

"""
while True:
    valuex = browser.find_element_by_xpath("//h5[@id='price']").text
    if valuex == "":
        print('Wait for it')
    elif int(valuex[1:]) == 100:
        browser.find_element_by_xpath("//button[@id='book']").click()
        break
"""

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element_by_xpath("//button[@id='book']").click()


valuey = int(browser.find_element_by_xpath("//span[@id='input_value']").text)
answer_temp = str(math.log(abs(12*math.sin(valuey))))
browser.find_element_by_xpath("//input[@id='answer']").send_keys(answer_temp)
browser.find_element_by_xpath("//button[@id='solve']").click()

alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
# answer = alert_text.split()[-1]
browser.quit()
