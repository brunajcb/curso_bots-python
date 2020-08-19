#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando bot.. \n")

#Getting Chrome control
driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver') 

#Accessing and capturing data
driver.get("http://turmalina.tce.pb.gov.br/avaliacao/<nome-do-muncipio>") #Trocar <nome-do-municipio> pelo nome do municipio como é definido na url do Turmalina TCE/pB
data = driver.find_elements_by_class_name("turmalina-data")
pontuacao_obtida = driver.find_elements_by_class_name("turmalina-ranking")
pontuacao_maxima = driver.find_elements_by_class_name("turmalina-ranking-max")

#Displaying results
print "A última avaliação de Cabedelo, feita pelo Turmalina, foi em:", (data[0].text)
print "A pontuação obtida foi de:", (pontuacao_obtida[0].text), "/", (pontuacao_maxima[0].text)
