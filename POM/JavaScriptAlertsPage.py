import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class JavaScriptAlertsPageLocators:
    jsAlertBtn = (By.CSS_SELECTOR, "#content li:nth-child(1)>button")
    jsConfirmBtn = (By.CSS_SELECTOR, "#content li:nth-child(2)>button")
    jsPromBtn = (By.CSS_SELECTOR, "#content li:nth-child(3)>button")
    msgResult = (By.CSS_SELECTOR, "#result")


class JavaScriptAlertsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectJsAlertBtn(self):
        self.driver.find_element(*JavaScriptAlertsPageLocators.jsAlertBtn).click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()

    def selectJsConfirmBtn(self):
        self.driver.find_element(*JavaScriptAlertsPageLocators.jsConfirmBtn).click()
        time.sleep(2)
        self.driver.switch_to_alert().dismiss()

    def selectJsPromBtn(self, name):
        time.sleep(2)
        self.driver.find_element(*JavaScriptAlertsPageLocators.jsPromBtn).click()
        time.sleep(3)
        alert = self.driver.switch_to_alert().send_keys(name)
        time.sleep(3)
        self.driver.switch_to_alert().accept()


    def getResultMessage(self):
        return self.driver.find_element(*JavaScriptAlertsPageLocators.msgResult)















