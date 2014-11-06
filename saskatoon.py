import getpass
import sys
from splinter import Browser
                    
with Browser() as browser:
    # Visit URL
    url = 'https://apps2.saskatoon.ca/lapp/eUtilAcct/AccountSummary.aspx'
    browser.visit(url)

    username = browser.find_by_xpath('//input[contains(@name, "Username")]')[0]
    username.fill(sys.argv[1])

    password = browser.find_by_xpath('//input[contains(@name, "Password")]')[0]
    password.fill(getpass.getpass())

    browser.find_by_xpath('//input[contains(@name, "Submit")]').first.click()

    figures = browser.find_by_xpath('//span[contains(text(), "$")]')
    for figure in figures:
        print figure.value
