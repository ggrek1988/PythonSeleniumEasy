#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
time.sleep(3)
source_element = driver.find_element_by_xpath("//span[text()='Draggable 2']")
dest_element = driver.find_element_by_xpath("//div[@id='mydropzone']")
print (source_element.text)
print (dest_element.text)
action = ActionChains(driver)
#.click_and_hold(source_element).move_to_element_with_offset(dest_element, 150, 200).perform()
#action.click_and_hold(source_element).pause(2).move_to_element(dest_element).perform()
action.drag_and_drop(source_element,dest_element).perform()
time.sleep(3)

