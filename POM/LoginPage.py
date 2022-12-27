import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class LoginPageLocators:
    btnLogin = (By.CSS_SELECTOR, '#login>button')
    redMsg = (By.ID, "flash")
    txtUserName = (By.ID, "username")
    txtPassword = (By.ID, "password")
    btnLogout = (By.CSS_SELECTOR, "#content>div>a")


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def selectBtnLogin(self):
        self.driver.find_element(*LoginPageLocators.btnLogin).click()

    def getErrorMessage(self):
        return self.driver.find_element(*LoginPageLocators.redMsg)

    def inputUserName(self, username):
        self.driver.find_element(*LoginPageLocators.txtUserName).send_keys(username)

    def inputPassword(self, password):
        self.driver.find_element(*LoginPageLocators.txtPassword).send_keys(password)

    def selectBtnLogout(self):
        return self.driver.find_element(*LoginPageLocators.btnLogout)

    def doLogin(self, username, password):
        self.driver.find_element(*LoginPageLocators.txtUserName).send_keys(username)
        self.driver.find_element(*LoginPageLocators.txtPassword).send_keys(password)
        self.driver.find_element(*LoginPageLocators.btnLogin).click()







