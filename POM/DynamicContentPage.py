import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DynamicContentPageLocators:
    textFirstParagraph = (By.CSS_SELECTOR, "#content>div:nth-child(1)>div.large-10.columns")
    textSecondParagraph = (By.CSS_SELECTOR, "content>div:nth-child(4)>div.large-10.columns")
    textThirdParagraph = (By.CSS_SELECTOR, "#content>div:nth-child(7)>div.large-10.columns")
    paragraphs = (By.CSS_SELECTOR, "#content > div")
    clickHereHyperlink = (By.CSS_SELECTOR, "#content>div>p:nth-child(3)>a")

class DynamicContentPage:

    def __init__(self, driver):
        self.driver = driver

    def returnTitleFirstParagraph(self):
        return self.driver.find_element(*DynamicContentPageLocators.textFirstParagraph).text

    def returnTitleSecondParagraph(self):
        return self.driver.find_element(*DynamicContentPageLocators.textSecondParagraph).text

    def returnTitleThirdParagraph(self):
        return self.driver.find_element(*DynamicContentPageLocators.textThirdParagraph).text

    def returnAllParagraphs(self):
        return self.driver.find_elements(*DynamicContentPageLocators.paragraphs)

    def clickHereLink(self):
        self.driver.find_element(*DynamicContentPageLocators.clickHereHyperlink).click()
