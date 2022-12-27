import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class InputsPageLocators:
    txtBox = (By.CSS_SELECTOR, "#content input[type=number]")



class InputsPage:

    def __init__(self, driver):
        self.driver = driver

    def insertNumberOnTheBox(self, num):
        time.sleep(3)
        self.driver.find_element(*InputsPageLocators.txtBox).send_keys(num)

    def increaseNumber(self):
        self.driver.find_element(*InputsPageLocators.txtBox).send_keys(Keys.ARROW_UP)

    def show_LastValue(self):
        return self.driver.find_element(*InputsPageLocators.txtBox).get_attribute("value")










