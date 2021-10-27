#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/bootstrap-progress-bar-dialog-demo.html")

driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()

try:
    driver.find_element_by_xpath('//div[@class="modal-header"]/h3[text()="Loading"]')
    print ("jest dobrze(1)")
    time.sleep(4)
    try:
        driver.find_element_by_xpath('//div[@class="modal fade in"]/div[@class="modal-dialog modal-m"]/div[@class="modal-content"]/div[@class="modal-header"]/h3[text()="Loading"]')
        print ("jest zle(2)")
    except:
        print("jest dobrze(2)")

except:
    print ("jest zle(1)")

