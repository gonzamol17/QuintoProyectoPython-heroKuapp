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
from POM.SibilingPage import SibilingPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestSibiling(BaseClass):

    def test_Sibiling(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clicklargeDeepLink()
        sp = SibilingPage(driver)
        aux1 = str(sp.getIndice())
        print("El Indice a buscar es :"+str(sp.getIndice()))
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 3000)")
        time.sleep(2)
        aux = sp.getAllNumbers()
        print("La cantidad de elementos para buscar el número obtenido, en esta fila son: "+str(len(sp.getAllNumbers())))
        for i in aux:
            print(i.text)
            if i.text == aux1:
                print("El valor: "+aux1+" fue encontrado en la lista, se detiene la búsqueda")
                break
            else:
                print("El valor no fue encontrado aún en la lista")
        time.sleep(2)

