import time
import pytest
import unittest
import sys
import os

from selenium.webdriver.common.keys import Keys

sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import json
from colorama import Fore, Back, Style
from Utils import utils as utils
from Utils.BaseClass import BaseClass
from POM.HomePage import HomePage
from POM.FileDownloadPage import FileDownloadPage
from selenium.webdriver import ActionChains


class TestFileDownload(BaseClass):

    def test_File_Download(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.fileDownloadLink()
        fd = FileDownloadPage(driver)
        fd.downloadImage()
        time.sleep(4)
        #.downloadTxt()
        while not os.path.exists('C:\\Users\\User\\Downloads'):
            time.sleep(2)
        # check file
        if os.path.isfile('C:\\Users\\User\\Downloads\\CheckDownload.txt'):
            time.sleep(2)
            print("File download is completed")
        else:
            time.sleep(2)
            print("File download is not completed")
        time.sleep(2)



