import os
import time
import unittest
# from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 755)
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_logging_to_system(self):
        user_login = LoginPage(self.driver)
        base_page = BasePage(self.driver)
        base_page.assert_element_text(self.driver, "//*[contains(text(),'Scouts Panel')]", 'Scouts Panel')
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.send_password('Test-1234')
        user_login.click_sign_in()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
