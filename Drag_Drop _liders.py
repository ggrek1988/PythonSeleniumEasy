#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains # symulacja myszy

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/drag-drop-range-sliders-demo.html")

en = driver.find_element_by_xpath("//div[@id='slider1']/div[@class='range']/input[@name='range']")
move = ActionChains(driver)
move.click_and_hold(en).move_by_offset(0, 20).release().perform()
sleep(5)
move.click_and_hold(en).move_by_offset(20, 50).release().perform()
sleep(5)

