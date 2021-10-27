from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


def WebDriverWait_byID(driver,pathadres,wait = 10 ):

    WebDriverWait(driver, wait).until(
        EC.presence_of_element_located((By.ID, pathadres))
    )