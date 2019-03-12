from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from SeleniumPom.Pages.loginPage import LoginPage
from SeleniumPom.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/Users/srinidhik/SeleniumWebdriver/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_Login(self):
        driver = self.driver

        driver.get('https://opensource-demo.orangehrmlive.com/')

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome_link()
        homepage.click_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")