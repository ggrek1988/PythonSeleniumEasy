from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

element = driver.find_element_by_id("isAgeSelected")
element.click()

element = driver.find_element_by_id("check1")
element.click()


liczba = 1
for x in range(1,5):

    button_element = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div['+str(liczba)+']/label/input')
    button_element.click()

    liczba = liczba+1
#button_element = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label/input')
#button_element.click()
#button_element = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[3]/label/input')
#button_element.click()
#button_element = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div[4]/label/input')
#button_element.click()