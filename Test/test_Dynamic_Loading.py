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
from POM.DynamicLoadingPage import DynamicLoadingPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestDynamicLoading(BaseClass):

    def test_DynamicLoading(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDynamicLoadingLink()
        dl = DynamicLoadingPage(driver)
        time.sleep(2)
        print("para saber si el parrafo primero está")
        assert str(dl.returnFirstParagraphTitle().is_displayed()) == "True"
        print("selecciono el primer hyperlink")
        dl.selectFirstLink()
        time.sleep(2)
        print("para saber si está el título nuevo, una vez que desaparece el primer párrafo")
        assert str(dl.returnNewTitle().is_displayed()) == "True"
        print("para saber cual es el título nuevo")
        print(dl.returnNewTitle().text)
        print("para saber si hay un botón Start")
        assert str(dl.returnStartBtn().is_displayed()) == "True"
        print("Se selecciona el botón Start")
        dl.returnStartBtn().click()
        time.sleep(5)
        print("El último título que se está visualizando al seleccionar el botón Start")
        assert str(dl.returnLastMsg()) == "Hello World!"
        print(dl.returnLastMsg())
        time.sleep(2)
        driver.back()
        #este comando de abajo es otra alternativa para hacer el driver.back, pero en javascript
        #driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        dl.selectSecondLink()
        time.sleep(2)
        assert "Example 2" in dl.returnNewTitleSecondExample()
        assert str(dl.returnStartBtn().is_displayed()) == "True"
        print("El botón start, está visualizandose correctamente")
        time.sleep(2)
