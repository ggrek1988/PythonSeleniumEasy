#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import random

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/table-records-filter-demo.html")

driver.find_element_by_xpath('//button[@data-target="pagado"]').click()
driver.find_element_by_xpath('//button[@data-target="pendiente"]').click()
driver.find_element_by_xpath('//button[@data-target="cancelado"]').click()
driver.find_element_by_xpath('//button[@data-target="all"]').click()