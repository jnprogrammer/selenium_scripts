import time
from selenium import webdriver

ChromeDriver = webdriver.Chrome()
#FireFoxDriver = webdriver.Firefox("/home/jnprogrammer/Projects/CareerDevs/Selenium/webDrivers/geckodriver")
ChromeDriver.get("https://www.circulation.com/")
#FireFoxDriver.get("https://www.xbox.com/")

print(ChromeDriver.title)
#print(ChromeDriver.find_element_by_id("h1"))

#print(FireFoxDriver.title)

time.sleep(5)
ChromeDriver.quit()
#FireFoxDriver.quit()