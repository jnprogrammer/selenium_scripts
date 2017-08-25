import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

#browser.get('http://www.yahoo.com')
browser.get('https://courses.ultimateqa.com/users/sign_in')
#assert 'Yahoo!' in browser.title

#elem = browser.find_element_by_id('uh-search-box')  # Find the search box  lst-ib
elem = browser.find_element_by_id('user_email')  # Find the search box  lst-ib
elem.send_keys('ThisisFAKE@NEEDHelp.com' + Keys.TAB)
elem = browser.find_element_by_id('user_password')
elem.send_keys('FakeAsFUCKPasswOrd' + Keys.ENTER)



time.sleep(15)
browser.quit()