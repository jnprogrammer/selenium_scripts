import time
from selenium import webdriver

Foxdriver = webdriver.Firefox()

Foxdriver.get("https://coinmarketcap.com/")

print(Foxdriver.title)

time.sleep(5)
Foxdriver.quit()