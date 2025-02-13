import time

from selenium.common import UnexpectedAlertPresentException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class JavaScriptAlertsPageLocators:
    jsAlertBtn = (By.XPATH, "//button[normalize-space()='Click for JS Alert']")
    jsConfirmBtn = (By.CSS_SELECTOR, "#content li:nth-child(2)>button")
    jsPromBtn = (By.CSS_SELECTOR, "#content li:nth-child(3)>button")
    msgResult = (By.CSS_SELECTOR, "#result")


class JavaScriptAlertsPage:

    def __init__(self, driver):
        self.driver = driver

    def selectJsAlertBtn(self):
        aux = self.driver.find_element(*JavaScriptAlertsPageLocators.jsAlertBtn).click()
        time.sleep(2)
        self.driver.switch_to.alert().accept()
        print("Timeout and No Alert Appearing")

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















