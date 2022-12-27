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
from POM.UploadPage import UploadPage
from selenium.webdriver import ActionChains

@pytest.mark.usefixtures("test_setup")
class TestFileUpload(BaseClass):

    def test_File_Upload(self):
        log = self.get_Logger()
        driver = self.driver
        hp = HomePage(driver)
        hp.fileUploadLink()
        up = UploadPage(driver)
        #up.openOptionToSelectFileBtn()
        time.sleep(2)
        aux = "C:\\Users\\admin\\Downloads\\asc.jpg"
        up.selectFile(aux)
        time.sleep(2)
        up.uploadFile()
        assert up.showTitleUploadedFile() == "File Uploaded!"
        #assert up.showTheFileUpload() == "asc.jpg"
        print("El Archivo está subido y es: "+up.showTheFileUpload())
        time.sleep(2)



