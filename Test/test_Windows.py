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
from POM.MultipleWindowsPage import MultipleWindowsPage

@pytest.mark.usefixtures("test_setup")
class TestWindows(BaseClass):

    def test_Windows(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        time.sleep(2)
        hp.clickMultipleWindowsLink()
        print("\nLa primera url es: "+driver.current_url)
        mp = MultipleWindowsPage(driver)
        parent_handle = driver.current_window_handle
        time.sleep(3)
        mp.selectHereHyperlink()
        driver.switch_to.window(driver.window_handles[1])
        print("La segunda url es: " + driver.current_url)
        time.sleep(2)
        handles = driver.window_handles
        size = len(handles)
        print("La cantidad de ventanas abiertas actualmente son "+str(size))
        for x in handles:
            driver.switch_to.window(x)
            #print(driver.current_url)
            if x != parent_handle:
                #driver.switch_to.window(x)
                print("El título de la segunda pestaña es: "+mp.getNewTitleWindows())
                time.sleep(2)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            else:
                print("El título de la primera pestaña es: "+mp.getFirstTitleWindows())
        time.sleep(3)



