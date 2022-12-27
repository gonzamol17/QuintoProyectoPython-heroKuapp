import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TablePageLocators:
    gralTable = (By.CSS_SELECTOR, "#table1>tbody>tr")




class TablePage:

    def __init__(self, driver):
        self.driver = driver



    def getAllNumbers(self):
        return self.driver.find_elements(*TablePageLocators.gralTable)

    def getNameByEachRecord(self, num, aux1):
        return self.driver.find_element(By.CSS_SELECTOR, "#table1>tbody>tr:nth-child(" + str(num) + ")>td:nth-child(" + str(aux1) + ")").text

    def getLastNameByEachRecord(self, num, aux1):
        return self.driver.find_element(By.CSS_SELECTOR, "#table1>tbody>tr:nth-child(" + str(num) + ")>td:nth-child(" + str(aux1+1) + ")").text

    def getWebsite(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, "#table1>tbody>tr:nth-child(" + str(num) + ")>td:nth-child(5)").text










