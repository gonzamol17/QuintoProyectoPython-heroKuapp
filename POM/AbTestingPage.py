import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AbTestingPageLocators:
    title = (By.CSS_SELECTOR, "#content>div>h3")


class AbTestingPage:

    def __init__(self, driver):
        self.driver = driver


    def sendTitle(self):
        return self.driver.find_element(*AbTestingPageLocators.title).text

