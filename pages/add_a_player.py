import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    click_to_add_player_xpath = "//span[text()='Add player']"
    expected_title_on_adding = 'Add player'
    add_players_name_xpath = "//input[@name='name']"
    add_players_surname_xpath = "//input[@name='surname']"
    add_players_age_xpath = "//input[@name='age']"
    add_players_main_position_xpath = "//input[@name='mainPosition']"
    add_players_submit_xpath = "//button[@type='submit']"

    def open_adding_player_form(self):
        self.click_on_the_element(self.click_to_add_player_xpath)

    def check_title_of_add_player_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title_on_adding

    def add_players_name(self, players_name):
        self.field_send_keys(self.add_players_name_xpath, players_name)

    def add_players_surname(self, players_surname):
        self.field_send_keys(self.add_players_surname_xpath, players_surname)

    def add_players_age(self, players_age):
        self.field_send_keys(self.add_players_age_xpath, players_age)

    def add_players_main_position(self, players_main_position):
        self.field_send_keys(self.add_players_main_position_xpath, players_main_position)

    def click_submit(self):
        self.click_on_the_element(self.add_players_submit_xpath)

