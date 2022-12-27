import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class HoversPageLocators:
    allimages = (By.CSS_SELECTOR, "#content>div img")
    getValue = (By.ID, "range")



class HoversPage:

    def __init__(self, driver):
        self.driver = driver

    def getAllImages(self):
        return self.driver.find_elements(*HoversPageLocators.allimages)

    def getAllInformationEachImage(self, images):
        num = 3
        nam = 1
        img = ActionChains(self.driver)
        users = ["user1", "user2", "user3"]
        for i in images:
            time.sleep(2)
            img.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "#content div:nth-child(" + str(num) + ")>img")).perform()
            time.sleep(3)
            aux = self.driver.find_element(By.CSS_SELECTOR, "#content div:nth-child(" + str(num) + ") h5").text
            assert aux == "name: user"+str(nam)
            print("Se ha encontrado el usuario "+str(nam))
            self.driver.find_element(By.CSS_SELECTOR, "#content div:nth-child(" + str(num) + ") a").click()
            time.sleep(3)
            self.driver.back()
            num = num+1
            nam = nam+1
            time.sleep(3)











