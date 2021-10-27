from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

for x in day:
    select = Select(driver.find_element_by_id('select-demo'))
    select.select_by_visible_text(''+str(x)+'')

city = ['California','Florida','New Jersey','New York','Ohio','Texas','Pennsylvania','Washington']
for x in city:
    for y in range(0,2):
        myElemA = driver.find_element_by_css_selector("option[value='" + str(x) + "']")
        ActionChains(driver).key_down(Keys.CONTROL).click(myElemA).key_up(Keys.CONTROL).perform()
        time.sleep(0.8)
        if y == 0:
            driver.find_element_by_xpath('//button[@id="printMe"]').click()


for x in city:
    myElemA = driver.find_element_by_css_selector("option[value='"+str(x)+"']")
    ActionChains(driver).key_down(Keys.CONTROL).click(myElemA).key_up(Keys.CONTROL).perform()
    time.sleep(0.8)

    driver.find_element_by_xpath('//button[@id="printAll"]').click()
