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
from POM.HorizontalSliderPage import HorizontalSliderPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestHorizontalSlider(BaseClass):

    def test_HorizontalSlider(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickhorizontalsliderLink()
        time.sleep(2)
        hs = HorizontalSliderPage(driver)
        hs.move_Switch(hs.getSwitchToMove(), 6)
        assert hs.showRange() == "2.5"
        print("Ahora el switch está en el rango de: "+hs.showRange())
        time.sleep(2)
        hs.move_Switch(hs.getSwitchToMove(), 60)
        assert hs.showRange() == "5"
        print("Ahora el switch está en el rango de: " + hs.showRange())
        time.sleep(2)





