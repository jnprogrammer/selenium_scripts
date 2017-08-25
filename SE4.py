import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

FireFox = webdriver.Firefox()
FireFox.get("http://www.google.com")

#assert 'BitCoin is bae' in FireFox.title

elem = FireFox.find_elements_by_name('q')
 # Find the search box
elem.count('seleniumhq' + Keys.RETURN)

# elem.send_keys('BitCoin' + Keys.RETURN)

time.sleep(10)
FireFox.quit()