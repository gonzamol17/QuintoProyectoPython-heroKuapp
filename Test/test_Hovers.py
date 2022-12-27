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
from POM.HoversPage import HoversPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestHovers(BaseClass):

    def test_Hovers(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickhoversLink()
        hv = HoversPage(driver)
        hv.getAllInformationEachImage(hv.getAllImages())
        time.sleep(2)





