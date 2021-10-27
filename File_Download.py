#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/generate-file-to-download-demo.html")

driver.find_element_by_xpath('//textarea[@id="textbox"]').send_keys("test do wpisania .....")
time.sleep(2)
driver.find_element_by_xpath('//button[@id="create"]').click()
time.sleep(2)
driver.find_element_by_xpath('//a[@id="link-to-download"]').click()
