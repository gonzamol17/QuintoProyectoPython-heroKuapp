import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DropDownPageLocators:
    titleDropdown = (By.CSS_SELECTOR, "#dropdown>option:nth-child(1)")
    dropdown = (By.ID, "dropdown")

class DropDownPage:

    def __init__(self, driver):
        self.driver = driver

    def returnTitleOfDropdown(self):
        return self.driver.find_element(*DropDownPageLocators.titleDropdown).text

    def selectSecondElementFromDropdown(self, n):
        select = Select(self.driver.find_element(*DropDownPageLocators.dropdown))
        select.select_by_value(n)





