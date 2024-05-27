import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Places")
class TestPlaces:
    @allure.title("Создание, редактирование, удаление Place")
    @pytest.mark.smoke
    @pytest.mark.place
    def test_create_new_place(self, authorization):
        page = MainPage()
        page.profile.open_places()
        page.place.click_add_new_place()
        place_name = page.place.create_new_place()
        page.place.open_place(place_name)
        page.place.checking_more_options()
        page.place.add_to_favorite()
        page.place.check_like_and_dislike_btn()
        page.place.click_group_chat_btn(place_name)
        page.place.test_chat()
        new_place_name = page.place.edit_place()
        page.place.open_place(new_place_name)
        page.place.delete_ad(new_place_name)

        # page.place.click_tab_around()
        # page.place.click_add_new_place()
        # page.place.create_new_place()

    @allure.title("Взаимодействие пользователя Place")
    @pytest.mark.smoke
    @pytest.mark.place
    def test_user_place(self, authorization):
        page = MainPage()
        page.profile.open_places()
        page.place.click_add_new_place()
        place_name = page.place.create_new_place()
        page.place.open_place(place_name)
        page.place.click_group_chat_btn(place_name)
        message = page.place.test_chat()
        page.place.click_back_btn()
        page.place.click_back_btn()
        page.login.logout()

        page.login.authorization(test_user_login, test_user_password)
        page.open_bottom_sheet()
        page.select_places_filter()

        page.user_open_place(place_name)
        page.place.checking_more_options_user_place(place_name)
        page.place.add_to_favorite()
        page.place.click_group_chat_btn(place_name)
        page.place.check_chat_msg(message)
        new_message = page.place.test_chat()
        # page.login.logout()
        #
        # page.login.authorization()
        # page.profile.open_places()
        # page.user_open_place(place_name)
        # page.place.check_chat_msg(new_message)
