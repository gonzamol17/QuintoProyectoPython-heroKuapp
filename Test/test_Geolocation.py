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
from POM.GeolocationPage import GeolocationPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestGeolocation(BaseClass):

    def test_geolocation(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickgeoLocationLink()
        time.sleep(2)
        gp = GeolocationPage(driver)
        time.sleep(2)
        aux = str(gp.verify_whereamIbtn().is_enabled())
        assert aux == "True"
        gp.verify_whereamIbtn().click()
        assert gp.showLatitude() == "44.8780063" or "-31.4385289"
        assert gp.showLongitude() == "-120.1933559" or "-64.2152589"
        print("De acuerdo a la geolocalización, estoy en Latitud: "+gp.showLatitude())
        print("De acuerdo a la geolocalización, estoy en Longitud: " + gp.showLongitude())
        time.sleep(2)





