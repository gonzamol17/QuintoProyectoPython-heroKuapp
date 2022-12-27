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
from POM.DragAndDropPage import DragAndDropPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestDragDrop(BaseClass):

    def test_DragDrop(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickDragAndDropLink()
        dd = DragAndDropPage(driver)
        print(dd.returnFirstBox().text)
        print(dd.returnSecondBox().text)
        time.sleep(2)
        dd.moveBoxAToBoxB(dd.returnFirstBox(), dd.returnSecondBox())
        print(dd.returnFirstBox().text)
        print(dd.returnSecondBox().text)
        time.sleep(3)
