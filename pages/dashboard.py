import time
import self as self

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'

    # dashboard_logo_path = "//div[1]/header/div/h6"
    # main_page_button_path = "//span[contains(text(),"Main page")]"
    # list_of_players_button_path = "//span[contains(text(),"Players")]"
    # select_language_button_path = "//span[contains(text(), "Polski")]"
    # sign_out_button_path = "//span[contains(text(), "Sign out")]"
    # players_count_info_path = "//div[contains(text(), "Players count")]"
    # matches_count_info_path = "//div[contains(text(),"Matches count")]"
    # reports_count_info_path = "//div[contains(text(),"Reports count")]"
    # events_count_info_path = "//div[contains(text(),"Events count")]"
    # logo_field_path = "//div[ @ title = 'Logo Scouts Panel']"
    # dev_team_contact_button_path = "//*[contains(text(),"Dev team contact")]"
    # add_player_button_path = "//a[contains(@href, 'https://app.slack.com/client/T3X4CAKNU/C3XTEGXB6')]"

    def title_of_page(self):
        time.sleep(4)
        print(self.get_page_title(self.dashboard_url))
        print(self.expected_title)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
