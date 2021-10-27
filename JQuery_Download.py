#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import random

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")

##The progress bar is designed to display the current percent complete for a process after clicking on 'Start Download' button
driver.find_element_by_xpath('//button[@id="downloadButton"]').click()


wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="ui-dialog-buttonset"]/button[text()="Close"]')))
element.click()