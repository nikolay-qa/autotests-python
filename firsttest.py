from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # code that fill in all the required fields
    input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
    input1.send_keys("Nikolay")
    input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
    input2.send_keys("Romeiko")
    input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
    input3.send_keys("test@test.com")

    # send filled form
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # check that registration is successful
    # Wait for page loading
    time.sleep(1)

    # find the element that contains the text
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # Assign to var welcome_text text from element welcome_text_elt.text
    welcome_text = welcome_text_elt.text

    # check with assert that expected text equal to text on the web page
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # pause for estimating of our test results
    time.sleep(10)
    # close the browser after all actions
    browser.quit()