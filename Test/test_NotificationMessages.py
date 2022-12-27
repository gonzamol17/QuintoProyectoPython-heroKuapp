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
from POM.NotificationMessages import NotificationMessagesPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestNotificationMessages(BaseClass):

    def test_NotificationMessages(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(2)
        hp.clickNotificationMessagesLink()
        time.sleep(2)
        nm = NotificationMessagesPage(driver)

        try:
            aux = str(nm.isPresentedSnackBar().is_enabled())
            assert "True" == aux
            print(nm.isPresentedSnackBar().text)
            time.sleep(2)
            nm.closeSnackBar()
            time.sleep(2)
            nm.selectHyperlink()
            time.sleep(2)
            print(nm.isPresentedSnackBar().text)
            time.sleep(2)

        except:
            nm.selectHyperlink()
            aux = str(nm.isPresentedSnackBar().is_enabled())
            assert "True" == aux
            print(nm.isPresentedSnackBar().text)
            time.sleep(2)






