from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

button1 = ['Male','Female']
for x in button1:
    button_element = driver.find_element_by_xpath("//input[@value='"+str(x)+"']")
    button_element.click()
    button = driver.find_element_by_xpath("//button[@id='buttoncheck']")
    button.click()

button2 = ['Male','Female']
age = ['0 - 5','5 - 15','15 - 50']
for x in button2:

    button_element = driver.find_element_by_xpath("//input[@value='"+str(x)+"'][@name='gender']")
    button_element.click()


    for y in age:
        button_element = driver.find_element_by_xpath("//input[@value='" + str(y) + "'][@name='ageGroup']")
        button_element.click()
        button = driver.find_element_by_xpath('//button[text()="Get values"]')
        button.click()