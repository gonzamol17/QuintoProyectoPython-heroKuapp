import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class FramesPageLocators:
    nestedLink = (By.CSS_SELECTOR, "#content li:nth-child(1)>a")
    iFrameLink = (By.CSS_SELECTOR, "#content li:nth-child(2)>a")
    titleIframe = (By.CSS_SELECTOR, "#content>div>h3")
    textArea = (By.ID, "tinymce")

class FramesPage:

    def __init__(self, driver):
        self.driver = driver

    def clickNestedLink(self):
        self.driver.find_element(*FramesPageLocators.nestedLink).click()

    def clickIframeLink(self):
        self.driver.find_element(*FramesPageLocators.iFrameLink).click()

    def showTitle(self):
        return self.driver.find_element(*FramesPageLocators.titleIframe).text

    def clickandWriteTextArea(self):
        self.driver.find_element(*FramesPageLocators.textArea).click()
        self.driver.find_element(*FramesPageLocators.textArea).send_keys("Estoy escribiendo acá a ver si se agrega")









