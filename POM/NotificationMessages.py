import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class NotificationMessagesPageLocators:
    blueSnackBar = (By.ID, "flash")
    iconToCloseSnackBar = (By.CSS_SELECTOR, "#flash>a")
    hyperlinkClick = (By.CSS_SELECTOR, "#content>div>p>a")



class NotificationMessagesPage:

    def __init__(self, driver):
        self.driver = driver

    def isPresentedSnackBar(self):
        return self.driver.find_element(*NotificationMessagesPageLocators.blueSnackBar)

    def closeSnackBar(self):
        self.driver.find_element(*NotificationMessagesPageLocators.iconToCloseSnackBar).click()

    def selectHyperlink(self):
        self.driver.find_element(*NotificationMessagesPageLocators.hyperlinkClick).click()








