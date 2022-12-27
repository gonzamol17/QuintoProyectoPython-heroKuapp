import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class RedirectLinkPageLocators:
    clickHere = (By.CSS_SELECTOR, "#redirect")
    code200 = (By.XPATH, "//a[contains(text(),'200')]")
    code301 = (By.XPATH, "//a[contains(text(),'301')]")
    code404 = (By.XPATH, "//a[contains(text(),'404')]")
    code500 = (By.XPATH, "//a[contains(text(),'500')]")
    listofcodes = (By.CSS_SELECTOR, "#content>div>ul>li")
    goBack = (By.CSS_SELECTOR, "#content>div>p>a")


class RedirectLink:

    def __init__(self, driver):
        self.driver = driver

    def clickHereHypelink(self):
        self.driver.find_element(*RedirectLinkPageLocators.clickHere).click()

    def clickCode200(self):
        self.driver.find_element(*RedirectLinkPageLocators.code200).click()

    def clickCode301(self):
        self.driver.find_element(*RedirectLinkPageLocators.code301).click()

    def clickCode404(self):
        self.driver.find_element(*RedirectLinkPageLocators.code404).click()

    def clickCode500(self):
        self.driver.find_element(*RedirectLinkPageLocators.code500).click()

    def getAllCodes(self):
        return self.driver.find_elements(*RedirectLinkPageLocators.listofcodes)

    def selectCode(self, num):
        self.driver.find_element(By.CSS_SELECTOR, "#content li:nth-child("+str(num)+")>a").click()

    def goBack(self):
        self.driver.find_element(*RedirectLinkPageLocators.goBack).click()











