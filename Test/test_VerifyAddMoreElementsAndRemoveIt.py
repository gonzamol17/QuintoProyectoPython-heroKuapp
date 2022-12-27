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
class TestAddMoreElementsAndRemoveIt(BaseClass):

    def test_AddMoreElementsAndRemoveIt(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        ar = AddRemoveElementsPage(driver)
        hp.clickAddRemoveLink()
        time.sleep(2)
        ar.selectAddelementBtn()
        n = 10
        for i in range(1, n):
            ar.selectAddelementBtn()
        time.sleep(2)
        m = ar.returnSelectDeleteBtn()
        aux = len(ar.returnSelectDeleteBtn())
        for i in m:
            ar.SelectIndividualDeleteBtn(aux)
            aux = aux-1
        print("Cantidad de botones agregados y borrados: "+str(n))
        time.sleep(3)


