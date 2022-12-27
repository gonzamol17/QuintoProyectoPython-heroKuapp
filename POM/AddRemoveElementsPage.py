import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AddRemoveElementsLocators:
    btnAddElement = (By.CSS_SELECTOR, "#content>div>button")
    btnRemoveElement = (By.CSS_SELECTOR, "#elements>button")


class AddRemoveElementsPage:

    def __init__(self, driver):
        self.driver = driver


    def selectAddelementBtn(self):
        self.driver.find_element(*AddRemoveElementsLocators.btnAddElement).click()

    def returnStatusOfDeleteBtn(self):
        return self.driver.find_element(*AddRemoveElementsLocators.btnRemoveElement).is_enabled()

    def returnSelectDeleteBtn(self):
        return self.driver.find_elements(*AddRemoveElementsLocators.btnRemoveElement)

    def SelectIndividualDeleteBtn(self, num):
        self.driver.find_element(By.CSS_SELECTOR, "#elements>button:nth-child("+str(num)+")").click()
