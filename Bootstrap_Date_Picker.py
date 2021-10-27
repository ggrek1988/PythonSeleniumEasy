#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import random

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")

#Date Example
driver.find_element_by_xpath('//input[@class="form-control"]').click()
driver.find_element_by_xpath('//th[@class="prev"]').click()
driver.find_element_by_xpath('//th[@class="next"]').click()
driver.find_element_by_xpath('//th[@class="today"]').click()
input = driver.find_element_by_xpath('//input[@class="form-control"]')
napis = (input.get_attribute('value'))
napis1 = int(napis[0:2])
driver.find_element_by_xpath('//input[@class="form-control"]').click()

driver.find_element_by_xpath('//th[@class="clear"]').click()
driver.find_element_by_xpath('//input[@class="form-control"]').click()
driver.find_element_by_xpath("//td[text()='"+str(napis1-1)+"']").click()
driver.find_element_by_xpath('//input[@class="form-control"]').click()
try:
    driver.find_element_by_xpath("//td[text()='"+str(napis1+1)+"']").click()
except:
    print ("bład w ustawianiu pózniejszej daty")
driver.find_element_by_xpath("//td[text()='"+str(napis1)+"']").click()

#Date Range Example :
driver.find_element_by_xpath('//div[@id="datepicker"]/input[@class="form-control"]').click()
driver.find_element_by_xpath('//th[@class="prev"]').click()
test = str(random.randint(1, 30))
driver.find_element_by_xpath("//td[text()='"+str(test)+"']").click()
driver.find_element_by_xpath('//div[@id="datepicker"]/input[@placeholder="End date"]').click()
driver.find_element_by_xpath('//th[@class="next"]').click()
test = str(random.randint(1, 30))
driver.find_element_by_xpath("//td[text()='"+str(test)+"']").click()