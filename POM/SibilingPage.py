import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SibilingPageLocators:
    indiceNam = (By.CSS_SELECTOR, "div#sibling-16\.1>:nth-child(1)")
    gralTable = (By.ID, "large-table")
    onlyTable = (By.CSS_SELECTOR, "#large-table > tbody > tr.row-16 >td")
    #onlyTable = (By.TAG_NAME, "td")




class SibilingPage:

    def __init__(self, driver):
        self.driver = driver

    def getIndice(self):
        return self.driver.find_element(*SibilingPageLocators.indiceNam).text

    def getAllNumbers(self):
        return self.driver.find_elements(*SibilingPageLocators.onlyTable)















