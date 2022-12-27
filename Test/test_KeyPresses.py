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
from POM.KeyPressesPage import KeyPressesPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestKeyPresses(BaseClass):

    def test_KeyPresses(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickKeyPressesLink()
        kp = KeyPressesPage(driver)
        kp.selectBackSpace()
        assert kp.getResultMsg().text == "You entered: BACK_SPACE"
        assert 'rgba(0, 128, 0, 1)' in kp.getResultMsg().value_of_css_property('color')
        time.sleep(3)
        kp.selectCtrl()
        assert kp.getResultMsg().text == "You entered: CONTROL"
        assert 'rgba(0, 128, 0, 1)' in kp.getResultMsg().value_of_css_property('color')
        time.sleep(3)
        kp.selectUp()
        assert kp.getResultMsg().text == "You entered: UP"
        assert 'rgba(0, 128, 0, 1)' in kp.getResultMsg().value_of_css_property('color')
        time.sleep(3)




