#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random


driver = webdriver.Firefox()

driver.get("https://www.seleniumeasy.com/test/jquery-dual-list-box-demo.html")
for x in range(0,4):
    liczba = random.randint(1, 14)
    select = Select(driver.find_element_by_xpath("//select[@class='form-control pickListSelect pickData']"))
    select.select_by_index(liczba);

driver.find_element_by_xpath('//button[@class="pAdd btn btn-primary btn-sm"]').click()
time.sleep(2)
driver.find_element_by_xpath('//button[@class="pAddAll btn btn-primary btn-sm"]').click()
time.sleep(2)
for x in range(0,4):
    liczba = random.randint(1, 14)
    select = Select(driver.find_element_by_xpath("//select[@class='form-control pickListSelect pickListResult']"))
    select.select_by_index(liczba);

driver.find_element_by_xpath('//button[@class="pRemove btn btn-primary btn-sm"]').click()
time.sleep(2)
driver.find_element_by_xpath('//button[@class="pRemoveAll btn btn-primary btn-sm"]').click()
