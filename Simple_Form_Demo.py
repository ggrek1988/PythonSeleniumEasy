from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

user_message = "1234"
sum1 = '2'
sum2 = '3'
driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
element = driver.find_element_by_id("user-message")
element.send_keys(user_message)
element = driver.find_element_by_id("sum1")
element.send_keys(sum1)
element = driver.find_element_by_id("sum2")
element.send_keys(sum2)
button_element = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
#ERROR:  Element <a class="button button-fleft searchButton" href="#"> is not clickable at point (577.6166763305664,225.06666564941406) because another element <div class="blockUI blockOverlay"> obscures it
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button"))).click()
button_element.click()

