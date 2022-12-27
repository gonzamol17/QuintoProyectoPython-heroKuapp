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
from POM.DropDownPage import DropDownPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestDropdown(BaseClass):

    def test_Dropdown(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDropDownLink()
        dd = DropDownPage(driver)
        print(dd.returnTitleOfDropdown())
        time.sleep(2)
        aux = dd.selectSecondElementFromDropdown('2')
        time.sleep(2)
