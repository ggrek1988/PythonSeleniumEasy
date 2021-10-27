from selenium import webdriver
import time
import url_website

driver = webdriver.Firefox()
driver.get(url_website.url_Bootstrap_Alert_messages)

driver.find_element_by_xpath('//button[@id="autoclosable-btn-success"]').click()
if driver.find_element_by_xpath('//button[@id="autoclosable-btn-success"]'):
    print('komunikat sie pojawil')
    time.sleep(6)
    if driver.find_element_by_xpath('//div[@style="display: none;"]'):
        print('dobrze: komunikat znika')

    elif driver.find_element_by_xpath('//div[@style="display: block;"]'):
        print ('zle komunikat nie znika')
else:
    print('komunikat sie nie pojawil')
###############
driver.find_element_by_xpath('//button[@id="normal-btn-success"]').click()

if driver.find_element_by_xpath('//div[@class="alert alert-success alert-normal-success"]'):
    print('komunikat sie pojawil')
    time.sleep(3)
    driver.find_element_by_xpath('//button[@class="close"]').click()

    if driver.find_element_by_xpath("//div[@class='alert alert-success alert-normal-success' and @style='display: none;']"):
        print('dobrze: komunikat znika')
    elif driver.find_element_by_xpath("//div[@class='alert alert-success alert-normal-success' and @style='display: block;']"):
        print ('zle komunikat nie znika')
else:
    print('komunikat sie nie pojawil')