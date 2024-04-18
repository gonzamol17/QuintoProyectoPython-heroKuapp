import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class EntryAdPageLocators:
    clickHereHyperlink = (By.CSS_SELECTOR, "#content p:nth-of-type(3)>a")
    closeBtnModal = (By.CSS_SELECTOR, "#modal div.modal-footer>p")
    textOfModal = (By.CSS_SELECTOR, "#modal div.modal-body>p")
    titleOfModal = (By.CSS_SELECTOR, "#modal div.modal-title > h3")

class EntryAdPage:

    def __init__(self, driver):
        self.driver = driver

    def clickCloseModal(self):
        self.driver.find_element(*EntryAdPageLocators.closeBtnModal).click()

    def returnTextOfModal(self):
        return self.driver.find_element(*EntryAdPageLocators.textOfModal).text

    def returnTitleOfModal(self):
        return self.driver.find_element(*EntryAdPageLocators.titleOfModal).text

    def clickClickHere(self):
        self.driver.find_element(*EntryAdPageLocators.clickHereHyperlink).click()








