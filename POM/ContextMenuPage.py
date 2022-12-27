import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ContextMenuPageLocators:
    boxArea = (By.CSS_SELECTOR, "#hot-spot")



class ContextMenuPage:

    def __init__(self, driver):
        self.driver = driver


    def selectrightClick(self):
        chains = ActionChains(self.driver)
        area = self.driver.find_element(*ContextMenuPageLocators.boxArea)
        chains.context_click(area).perform()
        time.sleep(1)
        self.driver.switch_to_alert().accept()

