#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import random

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/table-sort-search-demo.html")

driver.find_element_by_xpath("//select[@name='example_length']/option[text()='25']").click()

driver.find_element_by_xpath("//th[text()='Name']").click()
driver.find_element_by_xpath("//th[text()='Name']").click()

driver.find_element_by_xpath("//th[text()='Position']").click()
driver.find_element_by_xpath("//th[text()='Position']").click()

driver.find_element_by_xpath("//th[text()='Office']").click()
driver.find_element_by_xpath("//th[text()='Office']").click()