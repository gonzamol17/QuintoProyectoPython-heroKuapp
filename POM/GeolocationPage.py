import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class GeolocationPageLocators:
    whereamIBtn = (By.CSS_SELECTOR, "#content>div>button")
    latitude = (By.ID, "lat-value")
    longitude = (By.ID, "long-value")




class GeolocationPage:

    def __init__(self, driver):
        self.driver = driver

    def verify_whereamIbtn(self):
        return self.driver.find_element(*GeolocationPageLocators.whereamIBtn)

    def showLatitude(self):
        return self.driver.find_element(*GeolocationPageLocators.latitude).text

    def showLongitude(self):
        return self.driver.find_element(*GeolocationPageLocators.longitude).text









