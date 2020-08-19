#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando bot.. \n")

driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver') #api para acessar o chrome

driver.get("https://sogosolucoes.movidesk.com/Account/Login")

user = driver.find_element_by_name("UserName") 
user.clear()
user.send_keys("bruna")

password = driver.find_element_by_name("Password") 
password.clear() 
password.send_keys("tenteoutravez")
password.send_keys(Keys.RETURN)

time.sleep(2)