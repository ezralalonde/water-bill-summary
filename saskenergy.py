import getpass
import sys
from splinter import Browser
                    
with Browser() as browser:
    # Visit URL 
    url = 'https://myaccount.saskenergy.com/'
    browser.visit(url) 

    username = browser.find_by_xpath('//input[contains(@name, "username")]')[0]
    username.fill(sys.argv[1])

    password = browser.find_by_xpath('//input[contains(@name, "password")]')[0]
    password.fill(getpass.getpass())

    browser.find_by_xpath('//input[contains(@name, "signIn")]').first.click()
    money_xpath = '//font[contains(text(), "$")]'
    if browser.is_element_present_by_xpath(money_xpath, wait_time=5):
        # a 5-second timeout should be long enough for their redirect to finish
        figures = browser.find_by_xpath(money_xpath)
        for figure in figures:
            print figure.value
    else:
        print "Not available!? Look at the webpage."
        raw_input() # you should look at the webpage

