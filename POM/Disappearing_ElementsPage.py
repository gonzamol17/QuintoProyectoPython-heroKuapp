import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DisappearingElementsPageLocators:
    btnElements = (By.CSS_SELECTOR, "#content>div>ul>li")


class DisappearingElementsPage:

    def __init__(self, driver):
        self.driver = driver


    def QuantityButtons(self):
        return self.driver.find_elements(*DisappearingElementsPageLocators.btnElements)

    def getIndividualBtn(self, num):
        return self.driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(" + str(num) + ")>a")

