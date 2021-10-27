#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random


driver = webdriver.Firefox()

driver.get("https://www.seleniumeasy.com/test/data-list-filter-demo.html")

driver.find_element_by_xpath("//input[@id='input-search']").send_keys('Tyreese Burn')
time.sleep(2)
driver.find_element_by_xpath("//input[@id='input-search']").clear()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='input-search']").send_keys('Manager')
time.sleep(2)
driver.find_element_by_xpath("//input[@id='input-search']").clear()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='input-search']").send_keys('980-543-3333')
time.sleep(2)
driver.find_element_by_xpath("//input[@id='input-search']").clear()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='input-search']").send_keys('test5@company.com')