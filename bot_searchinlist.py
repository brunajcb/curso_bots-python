#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando bot.. \n")

#Reading excel
municipios = []
workbook = xlrd.open_workbook('pages.xlsx') 
sheet = workbook.sheet_by_index(0)

#Get lines
for linha in range(0,3):
    municipios.append(sheet.cell_value(linha,0))

#Getting Chrome control
driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver') 
driver.get("http://turmalina.tce.pb.gov.br/") 

for municipio in municipios:
    pesquisa = driver.find_element_by_id("mat-input-0")
    pesquisa.clear()
    pesquisa.send_keys(municipio)
    resultado = driver.find_elements_by_class_name("mat-option-text")
    clique = resultado[0].click()
    time.sleep(2)
    data = driver.find_elements_by_class_name("turmalina-data")
    pontuacao_obtida = driver.find_elements_by_class_name("turmalina-ranking")
    pontuacao_maxima = driver.find_elements_by_class_name("turmalina-ranking-max")
    time.sleep(2)
    #Displaying results
    print "A última avaliação de", municipio, "feita pelo Turmalina, foi em:", (data[0].text)
    print "A pontuação obtida foi de:", (pontuacao_obtida[0].text), "/", (pontuacao_maxima[0].text)
    restart = driver.find_elements_by_class_name("turmalina-app-name")
    back = restart[0].click()
    time.sleep(2)
driver.close()
