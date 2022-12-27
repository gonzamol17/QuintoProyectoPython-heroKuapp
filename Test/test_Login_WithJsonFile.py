import time
import pytest
import unittest
import json
from colorama import Fore, Back, Style
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
import HtmlTestRunner
from Utils import utils as utils
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))



@pytest.mark.usefixtures("test_setup")
class TestLoginWithJsonFile(BaseClass):

     def test_LoginWithJsonFile(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.formAutenticationLink()
        lp = LoginPage(driver)
        file = open("C:\\Users\\admin\\PycharmProjects\\heroKuapp\\Datos\\Login.json", "r")
        jsondata = file.read()
        obj = json.loads(jsondata)
        list = obj['users']
        for i in range(len(list)):
            username = list[i].get("user")
            password = list[i].get("password")
            lp.doLogin(username, password)
            print(Fore.BLUE + "Login con el usuario de " + username)
            aux = lp.getErrorMessage().text
            try:

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
                driver.get("https://the-internet.herokuapp.com/")
                hp.formAutenticationLink()
                time.sleep(2)

            except:

                if "Your username is invalid!" in aux:
                    assert "Your username is invalid!" in aux
                    assert lp.getErrorMessage().value_of_css_property('background-color') == "rgba(198, 15, 19, 1)"
                    print("No se ha podido hacer el login y ese visualiza el mensaje de error en rojo: " + lp.getErrorMessage().text)
                    driver.get("https://the-internet.herokuapp.com/")
                    hp.formAutenticationLink()
                    time.sleep(2)
                else:

                    assert "Your password is invalid!" in aux
                    assert lp.getErrorMessage().value_of_css_property('background-color') == "rgba(198, 15, 19, 1)"
                    print("No se ha podido hacer el login y ese visualiza el mensaje de error en rojo: " + lp.getErrorMessage().text)
                    driver.get("https://the-internet.herokuapp.com/")
                    hp.formAutenticationLink()
                    time.sleep(2)





