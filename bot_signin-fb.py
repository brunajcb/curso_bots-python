#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando bot.. \n")

#Getting Chrome control
driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver')

#Getting url, inserting access data and authenticating
driver.get("https://www.facebook.com/")

user = driver.find_element_by_id("email") 
user.clear()
user.send_keys("put your access email to facebook here")

password = driver.find_element_by_id("pass") 
password.clear() 
password.send_keys("put your password here")
password.send_keys(Keys.RETURN)

#Delay to being able follow the process - in seconds
time.sleep(2)