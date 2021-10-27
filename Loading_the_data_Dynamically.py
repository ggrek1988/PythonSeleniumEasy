#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver



driver = webdriver.Firefox()

driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")

driver.find_element_by_xpath('//button[@id="save"]').click()
