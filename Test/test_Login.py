import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestLogin(BaseClass):

     def test_WithIncorrectEmail(self):
         log = self.get_Logger()
         driver = self.driver
         hp = HomePage(driver)
         hp.formAutenticationLink()
         lp = LoginPage(driver)
         lp.inputUserName("tomsmit")
         time.sleep(2)
         lp.inputPassword("SuperSecretPassword!")
         time.sleep(2)
         lp.selectBtnLogin()
         time.sleep(2)
         aux = lp.getErrorMessage().text
         assert "Your username is invalid!" in aux
         assert lp.getErrorMessage().value_of_css_property('background-color') == "rgba(198, 15, 19, 1)"
         print("No se ha podido hacer el login y ese visualiza el mensaje de error en rojo: " + lp.getErrorMessage().text)


     def test_WithoutEmailandPassword(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.formAutenticationLink()
        lp = LoginPage(driver)
        lp.selectBtnLogin()
        time.sleep(2)
        aux = lp.getErrorMessage().text
        assert "Your username is invalid!" in aux
        assert lp.getErrorMessage().value_of_css_property('background-color') == "rgba(198, 15, 19, 1)"
        print("No se ha podido hacer el login y ese visualiza el mensaje de error en rojo: " + lp.getErrorMessage().text)
        time.sleep(2)


     def test_WithIncorrectPassword(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.formAutenticationLink()
        lp = LoginPage(driver)
        lp.inputUserName("tomsmith")
        time.sleep(2)
        lp.inputPassword("SuperSecretPassword")
        time.sleep(2)
        lp.selectBtnLogin()
        time.sleep(2)
        aux = lp.getErrorMessage().text
        assert "Your password is invalid!" in aux
        assert lp.getErrorMessage().value_of_css_property('background-color') == "rgba(198, 15, 19, 1)"
        print("No se ha podido hacer el login y ese visualiza el mensaje de error en rojo: " + lp.getErrorMessage().text)
        time.sleep(2)

     def test_WithEmailAndPassword(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.formAutenticationLink()
        lp = LoginPage(driver)
        lp.inputUserName("tomsmith")
        time.sleep(2)
        lp.inputPassword("SuperSecretPassword!")
        time.sleep(2)
        lp.selectBtnLogin()
        time.sleep(2)
        aux = lp.getErrorMessage().text
        assert "You logged into a secure area!" in aux
        assert lp.getErrorMessage().value_of_css_property('background-color') == "rgba(93, 164, 35, 1)"
        print("Se ha podido hacer el login exitosamente y ese visualiza el mensaje en verde: " + lp.getErrorMessage().text)
        time.sleep(2)
        aux1 = str(lp.selectBtnLogout().is_displayed())
        assert aux1 == "True"
        lp.selectBtnLogout().click()
        time.sleep(2)
        aux2 = lp.getErrorMessage().text
        assert "You logged out of the secure area!" in aux2
        assert lp.getErrorMessage().value_of_css_property('background-color') == "rgba(93, 164, 35, 1)"
        print("Se ha podido hacer el logout exitosamente y ese visualiza el mensaje en verde: " + lp.getErrorMessage().text)
        time.sleep(2)


