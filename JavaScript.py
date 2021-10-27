#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")

#JavaScript Alert Box
driver.find_element_by_xpath('//button[@class="btn btn-default"]').click()
time.sleep(2)
alert = driver.switch_to_alert()
alert.accept()

#JavaScript Confirm Box
time.sleep(2)
driver.find_element_by_xpath('//button[@class="btn btn-default btn-lg"]').click()
time.sleep(2)
alert = driver.switch_to_alert()
alert.accept()
time.sleep(2)
driver.find_element_by_xpath('//button[@class="btn btn-default btn-lg"]').click()
time.sleep(2)
alert = driver.switch_to_alert()
alert.dismiss()

#Java Script Alert Box
driver.find_element_by_xpath('//button[text()="Click for Prompt Box"]').click()
alert = driver.switch_to_alert()

alert.send_keys("tekst_wysylamy")
time.sleep(2)
alert.accept()

