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
from POM.JqueryMenuPage import JqueryMenuPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestJqueryMenu(BaseClass):

    def test_JqueryMenu(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickjqueryMenuLink()
        jm = JqueryMenuPage(driver)
        jm.selectEnabledItem()
        time.sleep(2)
        while not os.path.exists('C:\\Users\\admin\\Downloads'):
            time.sleep(2)
        # check file
        if os.path.isfile('C:\\Users\\admin\\Downloads\\menu.pdf'):
            time.sleep(2)
            print("PDF File download is completed")
        else:
            time.sleep(2)
            print("PDF File download is not completed")
        time.sleep(2)




