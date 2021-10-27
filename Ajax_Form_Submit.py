from selenium import webdriver
import time

import url_website
import WebDriverWait_def

driver = webdriver.Firefox()
driver.get(url_website.url_Ajax_Form_Submit)
name = 'Name name'
driver.find_element_by_xpath("//input[@name='title']").send_keys(''+str(name)+'')

description = 'description description description description description'
driver.find_element_by_xpath("//textarea[@name='description']").send_keys(''+str(description)+'')

driver.find_element_by_xpath('//input[@name="btn-submit"]').click()
driver.implicitly_wait(5) # seconds


try:
    WebDriverWait_def.WebDriverWait_byID(driver,'submit-control',10)

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

