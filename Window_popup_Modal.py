#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/window-popup-modal-demo.html")

#Single Window Popup

window_before = driver.window_handles[0]
window_before_title = driver.title
print(window_before_title)
driver.find_element_by_xpath('//a[@class="btn btn-primary followeasy" and text()="  Follow On Twitter "]').click()

time.sleep(5)

window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
window_after_title = driver.title
print(window_after_title)


if driver.find_element_by_xpath('//span[text()="Selenium Easy"]'):
    print('jestes na drugiej stronie')
    driver.close()
    driver.switch_to_window(window_before)

#Multiple Window Modal
time.sleep(2)
driver.find_element_by_xpath('//a[@id="followall"]').click()
time.sleep(5)
window_after_1 = driver.window_handles[1]
driver.switch_to_window(window_after_1)
window_after_title_1 = driver.title
print(window_after_title_1)
window_after_2 = driver.window_handles[2]
driver.switch_to_window(window_after_2)
window_after_title_2 = driver.title
print(window_after_title_2)
window_after_3 = driver.window_handles[3]
driver.switch_to_window(window_after_3)
window_after_title_3 = driver.title
print(window_after_title_3)