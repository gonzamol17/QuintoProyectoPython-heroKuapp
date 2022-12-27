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
from POM.InputsPage import InputsPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestInputs(BaseClass):

    def test_Inputs(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickinputsLink()
        ip = InputsPage(driver)
        ip.insertNumberOnTheBox(5)
        time.sleep(2)
        for i in range(1, 6):
            time.sleep(2)
            ip.increaseNumber()
        print("\nEl último valor que existe en el text field es: "+str(ip.show_LastValue()))
        time.sleep(2)





