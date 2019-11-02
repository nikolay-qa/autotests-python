from selenium import webdriver
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


def print_answer(remote: webdriver.Remote):     # function focus alert window and output data to console
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


try:
    input1 = browser.find_element_by_xpath("//input[@name='firstname']")
    input1.send_keys("Nikolay")
    input2 = browser.find_element_by_xpath("//input[@name='lastname']")
    input2.send_keys("Romeiko")
    input3 = browser.find_element_by_xpath("//input[@name='email']")
    input3.send_keys("test@test.com")

    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    current_dir = os.path.abspath(os.path.dirname(__file__))    # current path to this script
    file_path = os.path.join(current_dir, 'test.txt')           # adding file name to the current path

    print(os.path.abspath(__file__))    # current python script path
    print(os.path.abspath(os.path.dirname(__file__)))   # current dir path
    print(file_path)    # test.txt path

    file_upload1 = browser.find_element_by_xpath("//input[@id='file' and @accept='.txt']")
    file_upload1.send_keys(file_path)   # upload test.txt file to the site

    button1 = browser.find_element_by_xpath("//button[@type='submit']")
    button1.click()

    print_answer(browser)

finally:
     browser.quit()



