import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Market")
class TestMarket:
    @allure.title("Создание, редактирование, удаление AD Stuff")
    @pytest.mark.smoke
    @pytest.mark.market
    def test_create_new_ad_stuff(self, authorization):
        page = MainPage()
        page.profile.open_market()
        page.market.click_plus_new_market()
        page.market.click_create()
        ad_name = page.market.create_new_ad_stuff()
        page.market.open_market(ad_name)
        page.market.checking_more_options()
        page.market.open_market(ad_name)
        new_ad_name = page.market.edit_ad()
        page.market.open_market(new_ad_name)
        page.market.delete_ad(new_ad_name)

        # page.market.click_plus_new_market()
        # page.market.click_switch_sale_rent()
        # page.market.click_create()
        # ad_name = page.market.create_new_ad_stuff(permissions=False)
        # page.market.open_market(ad_name)
        # page.market.checking_more_options()
        # page.market.open_market(ad_name)
        # new_ad_name = page.market.edit_ad()
        # page.market.open_market(new_ad_name)
        # page.market.delete_ad(new_ad_name)

    @allure.title("Создание, редактирование, удаление AD Trasport")
    @pytest.mark.smoke
    @pytest.mark.market
    def test_create_new_ad_transport(self, authorization):
        page = MainPage()
        page.profile.open_market()
        page.market.click_plus_new_market()
        page.market.select_transportation_type_ad()
        page.market.click_create()
        ad_name = page.market.create_new_ad_transport()
        page.market.open_market(ad_name)
        page.market.checking_more_options()
        page.market.open_market(ad_name)
        page.market.delete_ad(ad_name)

    @allure.title("Создание, редактирование, удаление AD Housing")
    @pytest.mark.smoke
    @pytest.mark.market
    def test_create_new_ad_housing(self, authorization):
        page = MainPage()
        page.profile.open_market()
        page.market.click_plus_new_market()
        page.market.select_housing_type_ad()
        page.market.click_create()
        ad_name = page.market.create_new_ad_housing()
        page.market.open_market(ad_name)
        page.market.checking_more_options()
        page.market.open_market(ad_name)
        page.market.delete_ad(ad_name)

    @allure.title("Взаимодействие с пользователем")
    @pytest.mark.smoke
    @pytest.mark.market
    def test_create_new_ad_stuff(self, authorization):
        page = MainPage()
        page.profile.open_market()
        page.market.click_plus_new_market()
        page.market.click_create()
        ad_name = page.market.create_new_ad_stuff()
        page.pets.click_back_btn()
        page.login.logout()

        page.login.authorization(test_user_login, test_user_password)
        page.open_bottom_sheet()
        page.select_market_filter()
        page.user_open_ad(ad_name)
        page.market.click_contact_seller_btn()
        page.market.test_chat()

        page.login.logout()
        page.login.authorization()
        page.menu.open_chats()
        page.chats.check_market_message()

