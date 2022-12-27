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
from POM.TablesPage import TablePage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestTables(BaseClass):

    def test_Tables(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.tablesLink()
        tp = TablePage(driver)
        print("la cantidad de registros en la tabla es: "+str(len(tp.getAllNumbers())))
        aux = tp.getAllNumbers()
        num = 1
        aux1 = 1
        for i in aux:
            print("El usuario "+str(num)+" es: "+tp.getNameByEachRecord(num, aux1)+ " "+(tp.getLastNameByEachRecord(num, aux1)))
            if tp.getLastNameByEachRecord(num, aux1) == "Frank":
                assert tp.getWebsite(num) == "http://www.frank.com"
                print("Se encontró al usuario "+tp.getLastNameByEachRecord(num, aux1)+" y la web es: "+tp.getWebsite(num))
            num = num+1
        time.sleep(2)

