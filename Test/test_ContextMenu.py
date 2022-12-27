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
from POM.ContextMenuPage import ContextMenuPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestContextMenu(BaseClass):

    def test_ContextMenu(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickContextMenuLink()
        cm = ContextMenuPage(driver)
        cm.selectrightClick()
        time.sleep(2)
