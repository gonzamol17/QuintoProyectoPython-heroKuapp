import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class FloatingMenuPageLocators:
    allItemsMenu = (By.CSS_SELECTOR, "#menu>ul>li")
    btnHomeMenu = (By.XPATH, "//a[contains(text(),'Home')]")



class FloatingMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def getAllBtnMenu(self):
        return self.driver.find_elements(*FloatingMenuPageLocators.allItemsMenu)

    def selectHomeBtn(self):
        self.driver.find_element(*FloatingMenuPageLocators.btnHomeMenu).click()








