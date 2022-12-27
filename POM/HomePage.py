import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class HomePageLocators:
    abtestingLink = (By.CSS_SELECTOR, "#content>ul>li:nth-child(1)>a")
    addRemoveLink = (By.CSS_SELECTOR, "#content>ul>li:nth-child(2)>a")
    checkboxesLink = (By.CSS_SELECTOR, "#content>ul>li:nth-child(6)>a")
    contextMenuLink = (By.CSS_SELECTOR, "#content>ul>li:nth-child(7)>a")
    disappearingElementsLink = (By.XPATH, "//a[contains(text(), 'Disappearing Elements')]")
    dragAndDropLink = (By.XPATH, "//a[contains(text(), 'Drag and Drop')]")
    dropDownLink = (By.XPATH, "//a[contains(text(), 'Dropdown')]")
    dynamicContentLink = (By.XPATH, "//a[contains(text(), 'Dynamic Content')]")
    dynamicControlsLink = (By.XPATH, "//a[contains(text(), 'Dynamic Controls')]")
    dynamicLoadingLink = (By.XPATH, "//a[contains(text(), 'Dynamic Loading')]")
    entryAdLink = (By.XPATH, "//a[contains(text(), 'Entry Ad')]")
    fileDownloadLink = (By.XPATH, "//a[contains(text(), 'File Download')]")
    fileUploadLink = (By.XPATH, "//a[contains(text(), 'File Upload')]")
    floatingMenuLink = (By.XPATH, "//a[contains(text(), 'Floating Menu')]")
    formAuthenticationLink = (By.XPATH, "//a[contains(text(), 'Form Authentication')]")
    framesLink = (By.XPATH, "//a[contains(text(), 'Frames')]")
    geoLocationLink = (By.XPATH, "//a[contains(text(), 'Geolocation')]")
    horizontalSliderLink = (By.XPATH, "//a[contains(text(), 'Horizontal Slider')]")
    hoversLink = (By.XPATH, "//a[contains(text(), 'Hovers')]")
    scrollLink = (By.XPATH, "//a[contains(text(), 'Infinite Scroll')]")
    inputsLink = (By.XPATH, "//a[contains(text(), 'Inputs')]")
    jqueryMenuLink = (By.XPATH, "//a[contains(text(), 'JQuery UI Menus')]")
    javaScriptAlertsLink = (By.XPATH, "//a[contains(text(), 'JavaScript Alerts')]")
    keyPressesLink = (By.XPATH, "//a[contains(text(), 'Key Presses')]")
    largeDeepLink = (By.XPATH, "//a[contains(text(), 'Large & Deep DOM')]")
    multipleWindowsLink = (By.XPATH, "//a[contains(text(), 'Multiple Windows')]")
    notificationMessageLink = (By.XPATH, "//a[contains(text(), 'Notification Messages')]")
    redirectLink = (By.XPATH, "//a[contains(text(), 'Redirect Link')]")
    tablesLink = (By.XPATH, "//a[contains(text(), 'Sortable Data Tables')]")


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    def clickAbTestingLink(self):
        self.driver.find_element(*HomePageLocators.abtestingLink).click()

    def clickAddRemoveLink(self):
        self.driver.find_element(*HomePageLocators.addRemoveLink).click()

    def clickCheckboxesLink(self):
        self.driver.find_element(*HomePageLocators.checkboxesLink).click()

    def clickContextMenuLink(self):
        self.driver.find_element(*HomePageLocators.contextMenuLink).click()

    def clickDisappearingElementsLink(self):
        self.driver.find_element(*HomePageLocators.disappearingElementsLink).click()

    def clickDragAndDropLink(self):
        self.driver.find_element(*HomePageLocators.dragAndDropLink).click()

    def clickDropDownLink(self):
        self.driver.find_element(*HomePageLocators.dropDownLink).click()

    def clickDynamicContentLink(self):
        self.driver.find_element(*HomePageLocators.dynamicContentLink).click()

    def clickDynamicControlsLink(self):
        self.driver.find_element(*HomePageLocators.dynamicControlsLink).click()

    def clickDynamicLoadingLink(self):
        self.driver.find_element(*HomePageLocators.dynamicLoadingLink).click()

    def clickEntryAdLink(self):
        self.driver.find_element(*HomePageLocators.entryAdLink).click()

    def fileDownloadLink(self):
        self.driver.find_element(*HomePageLocators.fileDownloadLink).click()

    def fileUploadLink(self):
        self.driver.find_element(*HomePageLocators.fileUploadLink).click()

    def floatingMenuLink(self):
        self.driver.find_element(*HomePageLocators.floatingMenuLink).click()

    def formAutenticationLink(self):
        self.driver.find_element(*HomePageLocators.formAuthenticationLink).click()

    def clickframesLink(self):
        self.driver.find_element(*HomePageLocators.framesLink).click()

    def clickgeoLocationLink(self):
        self.driver.find_element(*HomePageLocators.geoLocationLink).click()

    def clickhorizontalsliderLink(self):
        self.driver.find_element(*HomePageLocators.horizontalSliderLink).click()

    def clickhoversLink(self):
        self.driver.find_element(*HomePageLocators.hoversLink).click()

    def clickscrollLink(self):
        self.driver.find_element(*HomePageLocators.scrollLink).click()

    def clickinputsLink(self):
        self.driver.find_element(*HomePageLocators.inputsLink).click()

    def clickjqueryMenuLink(self):
        self.driver.find_element(*HomePageLocators.jqueryMenuLink).click()

    def clickjavaScriptAlertLink(self):
        self.driver.find_element(*HomePageLocators.javaScriptAlertsLink).click()

    def clickKeyPressesLink(self):
        self.driver.find_element(*HomePageLocators.keyPressesLink).click()

    def clicklargeDeepLink(self):
        self.driver.find_element(*HomePageLocators.largeDeepLink).click()

    def clickMultipleWindowsLink(self):
        self.driver.find_element(*HomePageLocators.multipleWindowsLink).click()

    def clickNotificationMessagesLink(self):
        self.driver.find_element(*HomePageLocators.notificationMessageLink).click()

    def clickRedirectLink(self):
        self.driver.find_element(*HomePageLocators.redirectLink).click()

    def tablesLink(self):
        self.driver.find_element(*HomePageLocators.tablesLink).click()

