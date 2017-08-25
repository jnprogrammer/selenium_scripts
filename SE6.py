import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

#browser.get('http://www.yahoo.com')
browser.get('http://www.google.com')
#assert 'Yahoo!' in browser.title

#elem = browser.find_element_by_id('uh-search-box')  # Find the search box  lst-ib
elem = browser.find_element_by_id('lst-ib')  # Find the search box  lst-ib
elem.send_keys('seleniumhq' + Keys.RETURN)

for num in range(0,11):
    elem = browser.find_element_by_id('lst-ib')
    elem.clear()
    elem.send_keys("pictures of number " + str(num) + Keys.RETURN)

time.sleep(15)
browser.quit()