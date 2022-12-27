import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.keys import Keys

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.FloatingMenuPage import FloatingMenuPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestFileDownload(BaseClass):

    def test_Floating_Menu(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.floatingMenuLink()
        fm = FloatingMenuPage(driver)
        aux = fm.getAllBtnMenu()
        #print(len(fm.getAllBtnMenu()))
        lis1 = ['Home', 'News', 'Contact', 'About']
        n = 0
        for i in aux:
            var = i.text
            assert var == lis1[n]
            n = n+1
        driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        fm.selectHomeBtn()
        url = driver.current_url
        time.sleep(2)
        assert url == "https://the-internet.herokuapp.com/floating_menu#home"
        print("Se pudo seleccionar correctamente el botón Home, y se está en la url correcta: "+url)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(2)


