import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DragAndDropPageLocators:
    boxA = (By.ID, "column-a")
    boxB = (By.ID, "column-b")

class DragAndDropPage:

    def __init__(self, driver):
        self.driver = driver

    def returnFirstBox(self):
        return self.driver.find_element(*DragAndDropPageLocators.boxA)

    def returnSecondBox(self):
        return self.driver.find_element(*DragAndDropPageLocators.boxB)

    def moveBoxAToBoxB(self, a, b):
        ActionChains(self.driver).click_and_hold(a).move_to_element(b).perform()


