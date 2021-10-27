#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import random

lista = []
lista1 = ['a','b','e']

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/bootstrap-dual-list-box-demo.html")

wybor2 = random.choice(lista1)
driver.find_element_by_xpath('//input[@class="form-control"]').send_keys("{}".format(wybor2))

test = driver.find_element_by_xpath('//ul[@class="list-group"]')
items = test.find_elements_by_tag_name("li")
for item in items:
    text = item.text
    lista.append(text)
wybor1 = random.choice(lista)

while wybor1 == '':
    wybor1 = random.choice(lista)

if wybor1 == 'bootstrap-duallist':
    wybor1 = 'bootstrap-duallist '

print (wybor1)
driver.find_element_by_xpath('//ul[@class="list-group"]/li[text()="{}"]'.format(wybor1)).click()
time.sleep(2)
driver.find_element_by_xpath('//span[@class="glyphicon glyphicon-chevron-right"]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('//button[@class="btn btn-default btn-sm move-left"]').click()
