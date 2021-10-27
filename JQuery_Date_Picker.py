#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import random

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/jquery-date-picker-demo.html")

driver.find_element_by_xpath('//input[@id="from"]').click()
driver.find_element_by_xpath('//span[@class="ui-icon ui-icon-circle-triangle-w"]').click()
test = str(random.randint(1, 30))
driver.find_element_by_xpath("//a[text()='"+str(test)+"']").click()
driver.find_element_by_xpath('//input[@id="to"]').click()
test = str(random.randint(1, 30))
driver.find_element_by_xpath("//a[text()='"+str(test)+"']").click()