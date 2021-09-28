
from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from Sample.PageObjectModel.Pages.LoginPage import LoginPage
from Sample.PageObjectModel.Pages.HomePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    #unit testing functions

    #setup function

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= "C:\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    #test function

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(4)

    #teardown function
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Successfully Completed")

if __name__ == '__main__':

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/nehar/PycharmProjects/PythonSelenium/Reports'))













