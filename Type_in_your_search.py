#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import random

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")


#Type in your search to filter data by Tasks / Assignee / Status
lista = ['Wireframes','Mike Trout','completed','SEO tags','Emily John','deployed']
wybor1 = random.choice(lista)
driver.find_element_by_xpath('//input[@id="task-table-filter"]').click()
driver.find_element_by_xpath('//input[@id="task-table-filter"]').send_keys(str(wybor1))


#Click the filter icon to activate column filters inputs
lista = ['1','2','3','4','5']
lista1 = ['markino','jacobs','larrypt']
lista2 = ['Brigade','Daniel','Byron']
lista3 = ['Samuels','Karano','Swarroon']
driver.find_element_by_xpath('//button[@class="btn btn-default btn-xs btn-filter"]').click()
wybor1 = random.choice(lista)
driver.find_element_by_xpath('//input[@class="form-control"]').send_keys(str(wybor1))
driver.find_element_by_xpath('//button[@class="btn btn-default btn-xs btn-filter"]').click()

wybor1 = random.choice(lista1)
driver.find_element_by_xpath('//button[@class="btn btn-default btn-xs btn-filter"]').click()
driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys(str(wybor1))
driver.find_element_by_xpath('//button[@class="btn btn-default btn-xs btn-filter"]').click()

wybor1 = random.choice(lista2)
driver.find_element_by_xpath('//button[@class="btn btn-default btn-xs btn-filter"]').click()
driver.find_element_by_xpath('//input[@placeholder="First Name"]').send_keys(str(wybor1))
driver.find_element_by_xpath('//button[@class="btn btn-default btn-xs btn-filter"]').click()

wybor1 = random.choice(lista3)
driver.find_element_by_xpath('//button[@class="btn btn-default btn-xs btn-filter"]').click()
driver.find_element_by_xpath('//input[@placeholder="Last Name"]').send_keys(str(wybor1))
driver.find_element_by_xpath('//button[@class="btn btn-default btn-xs btn-filter"]').click()