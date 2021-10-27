#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import random

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/table-data-download-demo.html")

def zapis_do_pliku():
    lista = ['copy', 'csv', 'excel', 'pdf', 'print']
    wybor1 = random.choice(lista)
    if wybor1 != 'print':
        driver.find_element_by_xpath("//a[@class='dt-button buttons-" + str(wybor1) + " buttons-html5']").click()
    if wybor1 == 'print':
        driver.find_element_by_xpath("//a[@class='dt-button buttons-" + str(wybor1) + "']").click()
#Click on any of the option to Copy / Download / Print the data table.
zapis_do_pliku()
#Use search to filter records and Download data.
tablica1 = ['a','n','p','g']
wybor2 = random.choice(tablica1)
driver.find_element_by_xpath('//input[@type="search"]').click()
driver.find_element_by_xpath('//input[@type="search"]').send_keys(str(wybor2))
zapis_do_pliku()
#Use column sort option to sort data and download / print data in sorted order.

driver.find_element_by_xpath("//th[text()='Name']").click()
zapis_do_pliku()