# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import random
import string
import re

def phn():
    n = '00000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==[9]:
        n = str(random.randint(10**8, 10**10-1))
    return n[:3] + '' + n[3:6] + '' + n[6:9]



driver = webdriver.Firefox()
driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")

#name 41 znaków
rand1 = "".join( [random.choice(string.ascii_uppercase) for i in xrange(41)] )
driver.find_element_by_xpath("//input[@name='first_name']").send_keys(''+str(rand1)+'')
rand2 = "".join( [random.choice(string.ascii_uppercase) for i in xrange(41)] )
driver.find_element_by_xpath("//input[@name='last_name']").send_keys(''+str(rand2)+'')


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


email = str(random_char(7)) + "@gmail.com"

driver.find_element_by_xpath("//input[@name='email']").send_keys(''+str(email)+'')
email = driver.find_element_by_xpath("//input[@name='email']").get_attribute("value")


#validacja emaila
if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email): # if the email is valid
    print("dobry email!")
else:
    print("zly email!") # or raise exception to stop execution

number = '48 '+str(phn())


driver.find_element_by_xpath("//input[@name='phone']").send_keys(''+str(number)+'')
phone = driver.find_element_by_xpath("//input[@name='phone']").get_attribute("value")

#validacja telefonu
if re.match(r"(^[0-9]{2}(?: [0-9]{9})?$)", phone): # if the email is valid
    print("dobry telefon!")
else:
    print("zly telefon!") # or raise exception to stop execution

rand3 = "".join( [random.choice(string.ascii_uppercase) for i in xrange(41)] )
driver.find_element_by_xpath("//input[@name='address']").send_keys(''+str(rand3)+'')
rand4 = "".join( [random.choice(string.ascii_uppercase) for i in xrange(41)] )
driver.find_element_by_xpath("//input[@name='city']").send_keys(''+str(rand4)+'')

rand5 = random.randint(1,51)
#select = Select(driver.find_element_by_xpath("//select[@name='state']/option[text()='Alaska']"))
driver.find_element_by_xpath("//select[@name='state']/option["+str(rand5)+"]").click()

driver.find_element_by_xpath("//input[@name='zip']").send_keys('21-412')
zip = driver.find_element_by_xpath("//input[@name='zip']").get_attribute("value")
print zip
if re.match(r"(^[0-9]{2}(?:-[0-9]{3})?$)", str(zip)): # if the email is valid
    print("dobry kod pocztowy!")
else:
    print("zly kod pocztowy!") # or raise exception to stop execut