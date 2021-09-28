from selenium import webdriver
import time
import unittest
from PomProject.Pages.loginPage import loginPage
from PomProject.Pages.homePage import homePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/HP/PycharmProjects/seleniumProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def testLoginIsValid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = loginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        home = homePage(self.driver)
        home.click_welcome()
        home.click_logout()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test Completed")













