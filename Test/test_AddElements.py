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
from POM.AddRemoveElementsPage import AddRemoveElementsPage

@pytest.mark.usefixtures("test_setup")
class TestAddElements(BaseClass):

    def test_AddElements(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        ar = AddRemoveElementsPage(driver)
        hp.clickAddRemoveLink()
        time.sleep(2)
        ar.selectAddelementBtn()
        aux = str(ar.returnStatusOfDeleteBtn())
        assert aux == "True"
        time.sleep(3)

