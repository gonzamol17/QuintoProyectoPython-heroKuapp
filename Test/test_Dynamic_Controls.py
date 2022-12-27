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
from POM.DynamicControlsPage import DynamicControlsPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestDynamicControls(BaseClass):

    def test_DynamicControls(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDynamicControlsLink()
        dc = DynamicControlsPage(driver)
        dc.selectCheckbox()
        time.sleep(2)
        dc.selectBtnRemove()
        aux = str(dc.verifyCheckboxDissapear())
        assert aux == "True"
        time.sleep(2)
        aux1 = str(dc.verifyBtnAddExistence())
        assert aux1 == "True"
        time.sleep(2)
        aux2 = dc.verifyMessageItsGone()
        assert aux2 == "It's gone!"
        time.sleep(2)
        dc.selectBtnAdd()
        time.sleep(2)
        aux3 = dc.verifyMessageItsGone()
        assert aux3 == "It's back!"
        time.sleep(2)
        dc.selectNewCheckbox()
        time.sleep(2)
        aux4 = str(dc.verifyTxtEnable())
        assert aux4 == "False"
        time.sleep(2)
        dc.selectBtnEnable()
        time.sleep(3)
        dc.typeTextEnable("Now that the text field is enabled, i write this words")
        time.sleep(2)
        dc.selectBtnEnable()
        time.sleep(3)
        aux5 = str(dc.verifyTxtEnable())
        assert aux5 == "False"
        time.sleep(2)
        print(dc.returnTxtEnable())
        time.sleep(2)
