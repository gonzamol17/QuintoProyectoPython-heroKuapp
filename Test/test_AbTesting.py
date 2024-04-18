import time
import pytest
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.AbTestingPage import AbTestingPage


class TestAbTestingLink(BaseClass):

    def test_AbTestingLink(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        ab = AbTestingPage(driver)
        hp.clickAbTestingLink()
        assert "A/B Test Variation 1" == ab.sendTitle()
        time.sleep(2)

