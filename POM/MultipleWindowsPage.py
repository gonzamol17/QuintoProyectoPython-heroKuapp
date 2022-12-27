import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class MultipleWindowsPageLocators:
    clickHereHyperlink = (By.CSS_SELECTOR, "#content>div>a")
    newTitle = (By.CSS_SELECTOR, "body>div>h3")
    oldTitle = (By.CSS_SELECTOR, "#content>div>h3")


class MultipleWindowsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectHereHyperlink(self):
        self.driver.find_element(*MultipleWindowsPageLocators.clickHereHyperlink).click()

    def getNewTitleWindows(self):
        return self.driver.find_element(*MultipleWindowsPageLocators.newTitle).text

    def getFirstTitleWindows(self):
        return self.driver.find_element(*MultipleWindowsPageLocators.oldTitle).text










