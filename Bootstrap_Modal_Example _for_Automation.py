from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import url_website

driver = webdriver.Firefox()
driver.get(url_website.url_Bootstrap_Modal_Example_for_Automation)
#Single Modal Example
driver.find_element_by_xpath('//a[@class="btn btn-primary"]').click()
time.sleep(2)
if driver.find_element_by_xpath("//h4[@class='modal-title']"):
    print('dobrze: otworzenie okna')
else:
    print('zle: okno sie nie otworzylo')

driver.find_element_by_xpath('//a[@class="btn btn-primary" and text()="Save changes"]').click()

#Multiple Modal Example
time.sleep(2)
driver.find_element_by_xpath('//a[@href="#myModal"]').click()
time.sleep(2)
driver.find_element_by_xpath('//a[@href="#myModal2"]').click()
time.sleep(3)
wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal-footer:nth-child(6) > a:nth-child(2)")))
element.click()
