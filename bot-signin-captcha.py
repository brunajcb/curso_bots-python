#coding: utf-8
#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando bot.. \n")

#Getting Chrome control
driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver')

#Getting url and inserting access data
driver.get("put the url to access here")

user = driver.find_element_by_id("catch id from field username and put here") 
user.clear()
user.send_keys("put the username here")

password = driver.find_element_by_id("catch id from field password and put here") 
password.clear() 
password.send_keys("put the password here")

#Capturing the captcha question
captcha_question = driver.find_elements_by_class_name("catch class from captcha question and put here")
print captcha_question[0].text

#Sending the captcha answer and authenticating
captcha_answer = input('Insira o valor do captcha: ')
captcha = driver.find_element_by_id("catch id from answer field from captcha and put here")
captcha.clear()
captcha.send_keys(captcha_answer)

password.send_keys(Keys.RETURN)

#Delay to being able follow the process - in seconds
time.sleep(2)
