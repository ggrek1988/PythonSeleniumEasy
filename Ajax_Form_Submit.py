from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/ajax-form-submit-demo.html")
name = 'Name name'
driver.find_element_by_xpath("//input[@name='title']").send_keys(''+str(name)+'')

description = 'description description description description description'
driver.find_element_by_xpath("//textarea[@name='description']").send_keys(''+str(description)+'')

driver.find_element_by_xpath('//input[@name="btn-submit"]').click()
driver.implicitly_wait(5) # seconds


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "submit-control"))
    )
    print ('wczytuje')
finally:
    if driver.find_element_by_xpath('//div[@id="submit-control"]'):
        print 'wszystko gra'
        # write script

    else:
        print 'nic nie gra'
        script = "alert('nic nie gra')"

        # generate a alert via javascript
        driver.execute_script(script)

