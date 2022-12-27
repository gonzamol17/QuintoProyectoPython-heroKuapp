import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DynamicControlsPageLocators:
    checkbox = (By.CSS_SELECTOR, "#checkbox>input[type=checkbox]")
    btnRemove = (By.CSS_SELECTOR, "#checkbox-example>button")
    btnAdd = (By.CSS_SELECTOR, "#checkbox-example>button")
    msgGone = (By.CSS_SELECTOR, "#message")
    newCheckbox = (By.CSS_SELECTOR, "#checkbox")
    btnEnable = (By.CSS_SELECTOR, "#input-example>button")
    txtFieldEnable = (By.CSS_SELECTOR, "#input-example>input[type=text]")


class DynamicControlsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectCheckbox(self):
        self.driver.find_element(*DynamicControlsPageLocators.checkbox).click()

    def selectBtnRemove(self):
        self.driver.find_element(*DynamicControlsPageLocators.btnRemove).click()

    def verifyCheckboxDissapear(self):
        return self.driver.find_element(*DynamicControlsPageLocators.checkbox).is_displayed()

    def verifyBtnAddExistence(self):
        return self.driver.find_element(*DynamicControlsPageLocators.btnAdd).is_displayed()

    def verifyMessageItsGone(self):
        return self.driver.find_element(*DynamicControlsPageLocators.msgGone).text

    def selectBtnAdd(self):
        self.driver.find_element(*DynamicControlsPageLocators.btnAdd).click()

    def selectNewCheckbox(self):
        self.driver.find_element(*DynamicControlsPageLocators.newCheckbox).click()

    def selectBtnEnable(self):
        self.driver.find_element(*DynamicControlsPageLocators.btnEnable).click()

    def verifyTxtEnable(self):
        return self.driver.find_element(*DynamicControlsPageLocators.txtFieldEnable).is_enabled()

    def typeTextEnable(self, text):
        self.driver.find_element(*DynamicControlsPageLocators.txtFieldEnable).send_keys(text)

    def returnTxtEnable(self):
        return self.driver.find_element(*DynamicControlsPageLocators.txtFieldEnable).text











