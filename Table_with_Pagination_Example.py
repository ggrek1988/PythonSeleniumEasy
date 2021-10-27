#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import random

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/table-pagination-demo.html")

for x in range(0,2):
    driver.find_element_by_xpath('//a[@class="next_link"]').click()
for x in range(0,2):
    driver.find_element_by_xpath('//a[@class="prev_link"]').click()