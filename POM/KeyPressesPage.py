import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class KeyPressesPageLocators:
    resultMsg = (By.CSS_SELECTOR, "#result")
    txtField = (By.CSS_SELECTOR, "#target")



class KeyPressesPage:

    def __init__(self, driver):
        self.driver = driver

    def getResultMsg(self):
        return self.driver.find_element(*KeyPressesPageLocators.resultMsg)

    def selectBackSpace(self):
        self.driver.find_element(*KeyPressesPageLocators.txtField).send_keys(Keys.BACKSPACE)

    def selectCtrl(self):
        self.driver.find_element(*KeyPressesPageLocators.txtField).send_keys(Keys.CONTROL)

    def selectUp(self):
        self.driver.find_element(*KeyPressesPageLocators.txtField).send_keys(Keys.ARROW_UP)






