import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DynamicLoadingPageLocators:
    firstLink = (By.XPATH, "//a[contains(text(),'Example 1: Element on page that is hidden')]")
    secondLink = (By.XPATH, "//a[contains(text(),'Example 2: Element rendered after the fact')]")
    firstParagraphTitle = (By.CSS_SELECTOR, "p:nth-of-type(1)")
    newTitle = (By.CSS_SELECTOR, "#content>div>h4")
    startBtn = (By.CSS_SELECTOR, "#start>button")
    lastMessage = (By.XPATH, "//h4[contains(text(),'Hello World!')]")
    newTitleSecondHyperlink = (By.CSS_SELECTOR, "#content>div>h4")


class DynamicLoadingPage:

    def __init__(self, driver):
        self.driver = driver

    def selectFirstLink(self):
        self.driver.find_element(*DynamicLoadingPageLocators.firstLink).click()

    def selectSecondLink(self):
        self.driver.find_element(*DynamicLoadingPageLocators.secondLink).click()

    def returnFirstParagraphTitle(self):
        return self.driver.find_element(*DynamicLoadingPageLocators.firstParagraphTitle)

    def returnNewTitle(self):
        return self.driver.find_element(*DynamicLoadingPageLocators.newTitle)

    def returnStartBtn(self):
        return self.driver.find_element(*DynamicLoadingPageLocators.startBtn)

    def returnLastMsg(self):
        return self.driver.find_element(*DynamicLoadingPageLocators.lastMessage).text

    def returnNewTitleSecondExample(self):
        return self.driver.find_element(*DynamicLoadingPageLocators.newTitleSecondHyperlink).text
