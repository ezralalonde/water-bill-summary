import getpass
import sys
from splinter import Browser

with Browser() as browser:
    # Visit URL
    url = 'https://www.sasktel.com/iam/SasktelLogin.jsp'
    browser.visit(url)

    username = browser.find_by_xpath('//input[contains(@name, "username")]')[0]
    username.fill(sys.argv[1])

    password = browser.find_by_xpath('//input[contains(@name, "password")]')[0]
    password.fill(getpass.getpass())

    browser.find_by_xpath('//input[contains(@name, "submitaccount")]').first.click()

    figures = browser.find_by_xpath('//span[contains(text(), "$")]')
    for figure in figures:
        print figure.value
