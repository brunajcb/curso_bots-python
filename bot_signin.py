#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando bot.. \n")

#Getting Chrome control
driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver')

#Getting url, inserting access data and authenticating
driver.get("put the url to access here")

user = driver.find_element_by_name("UserName") 
user.clear()
user.send_keys("put the username here")

password = driver.find_element_by_name("Password") 
password.clear() 
password.send_keys("put the password here")
password.send_keys(Keys.RETURN)

#Delay to being able follow the process - in seconds
time.sleep(2)