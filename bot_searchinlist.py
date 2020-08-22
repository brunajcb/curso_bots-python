#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando bot.. \n")
arquivo = open("resultados.txt", "w")

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
    opcoesListadas = driver.find_elements_by_class_name("mat-option-text")
    clique = opcoesListadas[0].click()
    time.sleep(5)
    data = driver.find_elements_by_class_name("turmalina-data")
    pontuacao_obtida = driver.find_elements_by_class_name("turmalina-ranking")
    pontuacao_maxima = driver.find_elements_by_class_name("turmalina-ranking-max")
    time.sleep(5)
    #Displaying results
    texto = "A última avaliação de", municipio, "feita pelo Turmalina, foi em:", (data[0].text), "\n", "A pontuação obtida foi de:", (pontuacao_obtida[0].text), "/", (pontuacao_maxima[0].text)
    arquivo.write(str(texto))
    restart = driver.find_elements_by_class_name("turmalina-app-name")
    back = restart[0].click()
    time.sleep(20)

arquivo.close()
driver.close()
