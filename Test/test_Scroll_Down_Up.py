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
from POM.ScrollPage import ScrollPage
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("test_setup")
class TestScrollDownUp(BaseClass):

    def test_ScrollDownUp(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickscrollLink()
        sp = ScrollPage(driver)
        title = sp.getTitle()
        time.sleep(4)
        driver.execute_script("window.scrollBy(0, 100000);")
        time.sleep(3)
        print(sp.getthirdParagraph().is_enabled())
        time.sleep(3)
        actions = ActionChains(driver)
        actions.move_to_element(title).perform()
        time.sleep(2)





