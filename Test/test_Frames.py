import time
import pytest
import unittest
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.FramesPage import FramesPage
from selenium.webdriver import ActionChains
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
import HtmlTestRunner
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestFrames(BaseClass):

    def test_Frames(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.clickframesLink()
        time.sleep(2)
        fp = FramesPage(driver)
        fp.clickIframeLink()
        time.sleep(2)
        assert "An iFrame" in fp.showTitle()
        print(fp.showTitle())
        driver.switch_to.frame("mce_0_ifr")
        time.sleep(2)
        fp.clickandWriteTextArea()
        time.sleep(2)
        driver.switch_to.default_content()
        assert "An iFrame" in fp.showTitle()
        print(fp.showTitle())
        time.sleep(2)


