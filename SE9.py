import time
import highlight
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()


FirstName = "Phoenix"
LastName = "Wright"
Email = "AceAttorney@gmail.com"
PassWord = "changeThis_1"

browser.get('https://courses.ultimateqa.com/users/sign_in')



elem = browser.find_element_by_link_text('Create a new account')

highlight.highlight(elem) #highlights link about to be clicked

browser.implicitly_wait(5)
elem.click()

elem = browser.find_element_by_id('user_first_name')
elem.send_keys(FirstName)
elem = browser.find_element_by_id('user_last_name')
elem.send_keys(LastName)
elem = browser.find_element_by_id('user_email')
elem.send_keys(Email)
elem = browser.find_element_by_id('user_password')
elem.send_keys(PassWord + Keys.ENTER)

#copied
print()


time.sleep(5)
browser.quit()