from pages.base_page import BasePage


class AddMatch(BasePage):
    dashboard_scouts_panel_path = "//div[1]/header/div/h6"
    to_main_page_button_path = "//*[text()="Main page"]"
    players_list_button_path = "//span[contains(text(),"Players")]"
    account_button_path = "//div/ul[2]/div[1]/div[2]/span"
    matches_button_path = "//*[text()='Matches']"
    reports_button_path = "//span[contains(text(),"Reports")]"
    choose_polish_version_button_path = "//span[contains(text(),"Polski")]"
    sign_out_button_path = "//span[contains(text(),"Sign out")]"
    my_team_input_path = "//input[@name="myTeam"]"
    enemy_team_input_path = "//input[@name="enemyTeam"]"
    my_team_score_input_path = "//input[@type="number" and @name='myTeamScore']"
    enemy_team_score_input_path = "//input[@type="number" and @name='enemyTeamScore']"
    date_input_path = "//input[@type="date" and @name='date']"
    match_at_home_radiobutton_path = "//input[@type='radio' and name='matchAtHome'] | //span[contains(text(),"Match at home")]"
    match_out_home_radiobutton_path = "//input[@type='radio' and name='matchAtHome'] | //span[contains(text(),"Match out home")]"
    tshirt_color_input_path = "//input[@name="tshirt"]"
    league_input_path = "//input[@name="league"]"
    time_played_input_path = "//input[@name="timePlayed"]"
    number_input_path = "//input[@type="number" and @name="number"]"
    web_match_input_path = "//input[@type="text" and @name="webMatch"]"
    general_input_path = "//input[@type="text" and @name="general"]"
    rating_input_path = "//input[@type="number" and @name="rating"]"
    submit_addmatch_form_button_path = "//span[@class="MuiButton - label" and text()="Submit"]"
    clear_addmatch_form_button_path = "//span[@class="MuiButton - label" and text()="Clear"]"

