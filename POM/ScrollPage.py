import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ScrollPageLocators:
    title = (By.CSS_SELECTOR, "#content>div>h3")
    thirdParagraph = (By.CSS_SELECTOR, "#content > div > div > div > div > div:nth-child(3)")



class ScrollPage:

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*ScrollPageLocators.title)

    def getthirdParagraph(self):
        return self.driver.find_element(*ScrollPageLocators.thirdParagraph)













