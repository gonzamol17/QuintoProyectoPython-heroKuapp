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
from POM.JavaScriptAlertsPage import JavaScriptAlertsPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestJavaScriptAlerts(BaseClass):

    def test_JavaScriptAlerts(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickjavaScriptAlertLink()
        js = JavaScriptAlertsPage(driver)
        js.selectJsAlertBtn()
        time.sleep(2)
        print(js.getResultMessage().text)
        assert js.getResultMessage().text == "You successfully clicked an alert"
        assert 'rgba(0, 128, 0, 1)' in js.getResultMessage().value_of_css_property('color')
        time.sleep(2)
        js.selectJsConfirmBtn()
        time.sleep(2)
        print(js.getResultMessage().text)
        assert js.getResultMessage().text == "You clicked: Cancel"
        assert 'rgba(0, 128, 0, 1)' in js.getResultMessage().value_of_css_property('color')
        time.sleep(3)
        name = "Pedro"
        js.selectJsPromBtn(name)
        time.sleep(2)
        print(js.getResultMessage().text)
        assert js.getResultMessage().text == "You entered: "+name
        assert 'rgba(0, 128, 0, 1)' in js.getResultMessage().value_of_css_property('color')
        time.sleep(2)

