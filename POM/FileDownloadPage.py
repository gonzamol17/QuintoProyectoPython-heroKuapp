import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class FileDownloadPageLocators:
    firstImageLink = (By.CSS_SELECTOR, "#content>div>a:nth-child(2)")
    secondFileLink = (By.CSS_SELECTOR, "#content>div>a:nth-child(4)")


class FileDownloadPage:

    def __init__(self, driver):
        self.driver = driver

    def downloadImage(self):
        self.driver.find_element(*FileDownloadPageLocators.firstImageLink).click()

    def downloadTxt(self):
        self.driver.find_element(*FileDownloadPageLocators.secondFileLink).click()









