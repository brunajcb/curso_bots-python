#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando bot.. \n")

#Lendo do excel
pages = []
workbook = xlrd.open_workbook('pages.xlsx') 
sheet = workbook.sheet_by_index(0)

#Percorrendo as linhas
for linha in range(0,3):
    pages.append(sheet.cell_value(linha,0))


#Getting Chrome control
driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver') 
driver.get("https://caruaru.pe.gov.br/portal-da-transparencia/")

for page in pages:
    item = driver.find_elements_by_class_name()
    page.click()
    time.sleep(2)
    titulo = driver.find_element_by_tag_name("h2")
    print (titulo.text)
