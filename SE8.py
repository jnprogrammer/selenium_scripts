import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
#browser = webdriver.Firefox()
FirstName = "Phoenix"
LastName = "Wright"
Email = "AceAttorney@gmail.com"
PassWord = "changeThis_1"
#browser.get('http://www.yahoo.com')
browser.get('https://courses.ultimateqa.com/users/sign_in')
#assert 'Yahoo!' in browser.title

#elem = browser.find_element_by_id('uh-search-box')  # Find the search box  lst-ib
elem = browser.find_element_by_link_text('Create a new account')
browser.implicitly_wait(4)
elem.click()
#browser.wind
elem = browser.find_element_by_id('user_first_name')
elem.send_keys(FirstName)
elem = browser.find_element_by_id('user_last_name')
elem.send_keys(LastName)
elem = browser.find_element_by_id('user_email')
elem.send_keys(Email)
elem = browser.find_element_by_id('user_password')
elem.send_keys(PassWord + Keys.ENTER)

time.sleep(5)
browser.quit()