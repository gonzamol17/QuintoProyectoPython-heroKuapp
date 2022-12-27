import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class UploadPageLocators:
    openOptionToSelectFileBtn = (By.XPATH, '//input[@type="file"]')
    uploadFile = (By.ID, "file-submit")
    titleUploaded = (By.CSS_SELECTOR, "#content>div>h3")
    fileUpload = (By.ID, "uploaded-files")


class UploadPage:

    def __init__(self, driver):
        self.driver = driver

    def selectFile(self, path):
        time.sleep(2)
        self.driver.find_element(*UploadPageLocators.openOptionToSelectFileBtn).send_keys(path)
        time.sleep(3)

    def uploadFile(self):
        self.driver.find_element(*UploadPageLocators.uploadFile).click()

    def showTitleUploadedFile(self):
        return self.driver.find_element(*UploadPageLocators.titleUploaded).text

    def showTheFileUpload(self):
        return self.driver.find_element(*UploadPageLocators.fileUpload).text









