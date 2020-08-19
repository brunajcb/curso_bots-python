#coding: utf-8
#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando bot.. \n")

driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver') #api para acessar o chrome

driver.get("http://generico1.sogo.com.br/acesso")

user = driver.find_element_by_id("user_login") 
user.clear()
user.send_keys("bruna")

password = driver.find_element_by_id("user_pass") 
password.clear() 
password.send_keys("CmuRtW@)#YCe8@BA)%N@wLG#")

captcha_question = driver.find_elements_by_class_name("aiowps-captcha-equation")
print captcha_question[0].text

captcha_answer = input('Insira o valor do captcha: ')

captcha = driver.find_element_by_id("aiowps-captcha-answer")
captcha.clear()
captcha.send_keys(captcha_answer)

password.send_keys(Keys.RETURN)

time.sleep(2)
