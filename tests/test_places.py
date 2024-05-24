import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Market")
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
        page.place.click_group_chat_btn()
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
    def test_create_new_place(self, authorization):
        page = MainPage()
        page.profile.open_places()
        page.place.click_add_new_place()
        place_name = page.place.create_new_place()
        page.place.open_place(place_name)
        page.place.click_group_chat_btn()
        page.place.test_chat()
        page.pets.click_back_btn()
        page.pets.click_back_btn()
        page.login.logout()

        page.login.authorization(test_user_login, test_user_password)
        page.open_bottom_sheet()
        page.select_places_filter()

        page.user_open_ad(place_name)
        page.market.checking_more_options_user()
        page.market.add_to_favorite()
        page.market.click_contact_seller_btn()
        message = page.market.test_chat()
        page.login.logout()

