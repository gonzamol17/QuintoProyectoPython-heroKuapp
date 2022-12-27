import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils

from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.Disappearing_ElementsPage import DisappearingElementsPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestDisappearingElements(BaseClass):

    def test_DisappearingElements(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDisappearingElementsLink()
        de = DisappearingElementsPage(driver)
        cant = len(de.QuantityButtons())
        print("La cantidad de botones en esta pantalla es: "+str(cant))
        btn = de.QuantityButtons()
        n = 1
        for i in btn:
            print(i.text)
            hover = ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, "#content > div > ul > li:nth-child(" + str(n) + ")>a"))
            assert 'rgba(236, 236, 236, 1)' in de.getIndividualBtn(n).value_of_css_property('background-color')
            hover.perform()
            assert 'rgba(242, 242, 242, 1)' in de.getIndividualBtn(n).value_of_css_property('background-color')
            n = n+1
            time.sleep(2)
        time.sleep(2)
