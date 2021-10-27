import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select



driver = webdriver.Chrome()
# driver.maximize_window()
driver = webdriver.Firefox()
driver.get("http://html5demos.com/drag")
target = driver.find_element_by_id("one")
source = driver.find_element_by_id("bin")
actionChains = ActionChains(driver)
actionChains.drag_and_drop(target, source).perform()

time.sleep(2)
