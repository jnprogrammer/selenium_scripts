import time
import userData
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#application will open a website scroll to input fields and enter in data.

chrome = webdriver.Chrome()

chrome.get("https://www.ultimateqa.com/complicated-page/")
actions = ActionChains(chrome)

msgElement = chrome.find_element_by_id("et_pb_contact_message_2")

actions.move_to_element(msgElement).perform()

element = chrome.find_element_by_id('et_pb_contact_name_2')
element.send_keys(userData.FirstName + " " + userData.LastName)

element = chrome.find_element_by_id('et_pb_contact_email_2')
#chrome.execute_script("window.scrollTo(50,document.body.scrollHeight);") et_pb_contact_name_2
element.send_keys(userData.Email)

msgElement.send_keys(userData.Phone)

captaElement = chrome.find_element_by_name("et_pb_contact_captcha_2")
#currentCaptaText = chrome.find_element_by_id()
captaElement.send_keys('12')
time.sleep(15)
chrome.quit()