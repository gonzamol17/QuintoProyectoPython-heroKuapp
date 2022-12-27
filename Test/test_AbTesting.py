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
from POM.AbTestingPage import AbTestingPage

@pytest.mark.usefixtures("test_setup")
class TestAbTestingLink(BaseClass):

    def test_AbTestingLink(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        ab = AbTestingPage(driver)
        hp.clickAbTestingLink()
        assert "A/B Test Control" == ab.sendTitle()
        time.sleep(2)

