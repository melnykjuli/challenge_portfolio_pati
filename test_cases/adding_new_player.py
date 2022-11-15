import os
import time
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.add_a_player import AddPlayer
from pages.login_page import LoginPage
from test_cases import login_to_the_system
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddNewPlayer(unittest.TestCase):

    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 755)
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.send_password('Test-1234')
        user_login.click_sign_in()
        dashboard_page = Dashboard(self.driver)
        time.sleep(5)
        add_new_player = AddPlayer(self.driver)
        add_new_player.open_adding_player_form()
        add_new_player.check_title_of_add_player_page()
        add_new_player.add_players_name('TEST1')
        add_new_player.add_players_surname('TEST1_1')
        add_new_player.add_players_age('15.11.2022')
        add_new_player.add_players_main_position('main')
        add_new_player.click_submit()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
