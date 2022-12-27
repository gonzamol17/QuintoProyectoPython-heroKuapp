import collections
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
from POM.DynamicContentPage import DynamicContentPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestDynamicContent(BaseClass):

    def test_DynamicContent(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDynamicContentLink()
        dc = DynamicContentPage(driver)
        #first_paragraph = dc.returnTitleFirstParagraph()
        #second_paragraph = dc.returnTitleSecondParagraph()
        #third_paragraph = dc.returnTitleThirdParagraph
        aux1 = dc.returnAllParagraphs()
        list1 = []
        n = 1
        for i in aux1:
            if n == 1:
                #print("No sumarlo")
                n = n+1

            else:
                list1.append(i.text)
                n = n+1
        print(list1)
        time.sleep(3)
        dc.clickHereLink()
        time.sleep(1)
        aux2 = dc.returnAllParagraphs()
        list2 = []
        m = 1
        for i in aux2:
            if m == 1:
                #print("No sumarlo")
                m = m+1

            else:
                list2.append(i.text)
                m = m+1
        print(list2)

        # esta es una forma de comparar dos listas y ver si son iguales entre ellas
        #if collections.Counter(list1) == collections.Counter(list2):
        #    print("Las listas son iguales")
        #else:
        #    print("Las listas no son iguales, los segundos párrafos son distintos a los primeros, estamos ante contenido dinámico")

        # esta es otra forma de comparar dos listas y ver si son iguales entre ellas
        if set(list1) == set(list2):
            print("Las listas son iguales")
        else:
            print("Las listas no son iguales, los segundos párrafos son distintos a los primeros, estamos ante contenido dinámico")
        url = driver.current_url
        assert url == "https://the-internet.herokuapp.com/dynamic_content?with_content=static"
        time.sleep(3)
