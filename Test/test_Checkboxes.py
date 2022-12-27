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
from POM.CheckboxesPage import CheckboxesPage

@pytest.mark.usefixtures("test_setup")
class TestCheckboxes(BaseClass):

    def test_Checkboxes(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickCheckboxesLink()
        cb = CheckboxesPage(driver)
        aux = str(cb.verifyCheckboxIsSelected())
        assert aux == "True"
        time.sleep(2)
        cb.selectSecondCheckbox()
        time.sleep(2)
        cb.selectFirstCheckbox()
        time.sleep(2)
        cb.selectSecondCheckbox()
        time.sleep(2)
