import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()

#browser.get('http://www.yahoo.com')
browser.get('http://www.google.com')
#assert 'Yahoo!' in browser.title

#elem = browser.find_element_by_id('uh-search-box')  # Find the search box  lst-ib
elem = browser.find_element_by_id('lst-ib')  # Find the search box  lst-ib
elem.send_keys('seleniumhq' + Keys.RETURN)

time.sleep(12)
browser.quit()