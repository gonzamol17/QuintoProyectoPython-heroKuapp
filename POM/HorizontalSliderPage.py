import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class HorizontalSliderPageLocators:
    switch = (By.CSS_SELECTOR, "#content input[type=range]")
    getValue = (By.ID, "range")



class HorizontalSliderPage:

    def __init__(self, driver):
        self.driver = driver

    def getSwitchToMove(self):
        return self.driver.find_element(*HorizontalSliderPageLocators.switch)

    def move_Switch(self, switch, value):
        time.sleep(2)
        ActionChains(self.driver).drag_and_drop_by_offset(switch, value, 0).perform()

    def showRange(self):
        return self.driver.find_element(*HorizontalSliderPageLocators.getValue).text











