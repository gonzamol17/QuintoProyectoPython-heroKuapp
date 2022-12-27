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
from POM.RedirectLink import RedirectLink
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestRedirectLink(BaseClass):

    def test_RedirectLink(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(2)
        hp.clickRedirectLink()
        time.sleep(2)
        rl = RedirectLink(driver)
        time.sleep(2)
        rl.clickHereHypelink()
        cant = len(rl.getAllCodes())
        aux = 1
        list1 = []
        list2 = ['https://the-internet.herokuapp.com/status_codes/200', 'https://the-internet.herokuapp.com/status_codes/301', 'https://the-internet.herokuapp.com/status_codes/404', 'https://the-internet.herokuapp.com/status_codes/500']
        print("La cantidad de códigos listados es: "+str(cant))
        aux1 = rl.getAllCodes()
        n = 0
        for i in aux1:
            #time.sleep(2)
            rl.selectCode(aux)
            #time.sleep(2)
            aux = aux+1
            #print(driver.current_url)
            assert driver.current_url in list2
            print("en la lista está el código: "+list2[n])
            list1.append(driver.current_url)
            n = n+1
            rl.goBack()

        #n = 0
        #for i in list1:
        #    assert i in list2[n]
        #    n = n+1
        time.sleep(2)





