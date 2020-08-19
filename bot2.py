#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando bot.. \n")

driver = webdriver.Chrome('/Users/bruna/desktop/bots/chromedriver') #api para acessar o chrome

driver.get("http://turmalina.tce.pb.gov.br/avaliacao/Cabedelo")
data = driver.find_elements_by_class_name("turmalina-data")
pontuacao_obtida = driver.find_elements_by_class_name("turmalina-ranking")
pontuacao_maxima = driver.find_elements_by_class_name("turmalina-ranking-max")

print "A última avaliação de Cabedelo, feita pelo Turmalina, foi em:", (data[0].text)
print "A pontuação obtida foi de:", (pontuacao_obtida[0].text), (pontuacao_maxima[0].text)
print pontuacao_obtida
print (pontuacao_obtida[0].text)
