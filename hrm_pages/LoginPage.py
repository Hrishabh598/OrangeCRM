from hrm_helper.selenium_helper import Selenium_Helper
from selenium.webdriver.common.by import By

class LoginPage(Selenium_Helper):

    username_webElement = (By.XPATH,"//input[@name='username']")
    password_webElement = (By.XPATH,"//input[@name='password']")
    loginBtn_webElement = (By.XPATH,"//button")

    def __init__(self,driver):
        super().__init__(driver)

    def login(self,username,password):
        self.webelement_enter(self.username_webElement,username)
        self.webelement_enter(self.password_webElement,password)
        self.webelement_click(self.loginBtn_webElement)



