import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class JqueryMenuPageLocators:
    enabledItem = (By.CSS_SELECTOR, "#ui-id-3>a")
    downloadItem = (By.CSS_SELECTOR, "#ui-id-4>a")
    pdfItem = (By.CSS_SELECTOR, "#ui-id-5>a")



class JqueryMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def selectEnabledItem(self):
        item = ActionChains(self.driver)
        item.move_to_element(self.driver.find_element(*JqueryMenuPageLocators.enabledItem)).perform()
        time.sleep(2)
        item.move_to_element(self.driver.find_element(*JqueryMenuPageLocators.downloadItem)).perform()
        time.sleep(2)
        item.move_to_element(self.driver.find_element(*JqueryMenuPageLocators.pdfItem)).perform()
        self.driver.find_element(*JqueryMenuPageLocators.pdfItem).click()












