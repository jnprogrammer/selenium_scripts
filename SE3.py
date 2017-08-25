import time
from selenium import webdriver

OpDriver = webdriver.Opera()

OpDriver.get("https://coinmarketcap.com/")

print(OpDriver)

time.sleep(20)
OpDriver.quit()