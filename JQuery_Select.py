from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/jquery-dropdown-search-demo.html")

tablica = ['a','b','d','h','i','j','n','s','u']

#Drop Down with Search box
wybor = random.choice(tablica)
driver.find_element_by_xpath('//span[@class="select2-selection select2-selection--single"]').click()
driver.find_element_by_xpath('//span[@class="select2-search select2-search--dropdown"]/input[@class="select2-search__field"]').send_keys(str(wybor))
driver.find_element_by_xpath('//span[@class="select2-search select2-search--dropdown"]/input[@class="select2-search__field"]').send_keys(Keys.ENTER)


#Select Multiple
for x in range(0,5):
    wybor = random.choice(tablica)
    driver.find_element_by_xpath('//span[@class="select2-selection select2-selection--multiple"]').click()
    driver.find_element_by_xpath('//input[@class="select2-search__field"]').send_keys(str(wybor))
    driver.find_element_by_xpath('//input[@class="select2-search__field"]').send_keys(Keys.ENTER)

for x in range(0,2):
    driver.find_element_by_xpath('//span[@class="select2-selection__choice__remove"]').click()

driver.find_element_by_xpath('//span[@class="select2-selection select2-selection--multiple"]').click()

#Drop Down with Disabled values
#text_list = [e.text for e in driver.find_elements_by_xpath('//span[@class="select2-selection select2-selection--single"]')]
#print (text_list)
tablica1 = ['a','n','p','g']

#Drop Down with Search box
wybor1 = random.choice(tablica1)
driver.find_elements_by_xpath('//span[@class="select2-selection select2-selection--single"]')[1].click()
driver.find_elements_by_xpath('//input[@class="select2-search__field"]')[1].send_keys(str(wybor1))
driver.find_elements_by_xpath('//input[@class="select2-search__field"]')[1].send_keys(Keys.ENTER)

#Drop-down with Category related options

tablica2 = ['jquery','jqueryui','pjqueryui','somefile','someotherfile']

wybor2 = random.choice(tablica2)

driver.find_elements_by_xpath('//select[@id="files"]')[0].click()
driver.find_element_by_xpath("//option[@value='"+(str(wybor2))+"']").click()

