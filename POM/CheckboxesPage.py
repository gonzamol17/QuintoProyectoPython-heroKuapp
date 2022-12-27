import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class CheckboxesPageLocators:
    secondCheckbox = (By.CSS_SELECTOR, "#checkboxes>input[type=checkbox]:nth-child(3)")
    firstCheckbox = (By.CSS_SELECTOR, "#checkboxes>input[type=checkbox]:nth-child(1)")


class CheckboxesPage:

    def __init__(self, driver):
        self.driver = driver


    def verifyCheckboxIsSelected(self):
        return self.driver.find_element(*CheckboxesPageLocators.secondCheckbox).is_selected()

    def selectSecondCheckbox(self):
        self.driver.find_element(*CheckboxesPageLocators.secondCheckbox).click()

    def selectFirstCheckbox(self):
        self.driver.find_element(*CheckboxesPageLocators.firstCheckbox).click()

