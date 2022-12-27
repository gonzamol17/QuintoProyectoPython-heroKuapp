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
from POM.EntryAdPage import EntryAdPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestEntryAd(BaseClass):

    def test_EntryAd(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickEntryAdLink()
        time.sleep(3)
        ea = EntryAdPage(driver)
        assert "It's commonly" in ea.returnTitleOfModal()
        ea.clickCloseModal()
        ea.clickClickHere()
        time.sleep(3)
        print("Se está visualizando nuevamente el modal, y el título es : \n"+ea.returnTitleOfModal())
        time.sleep(2)


