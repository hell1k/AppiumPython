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
        page.market.add_to_favorite()
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

    @allure.title("Проверка отправки всех типов медиа в чат MARKET")
    @pytest.mark.smoke
    @pytest.mark.market
    @pytest.mark.chats
    def test_market_chat(self, authorization):
        # Создаем объявление пользователем 1
        page = MainPage()
        page.profile.open_market()
        page.market.click_plus_new_market()
        page.market.click_create()
        ad_name = page.market.create_new_ad_stuff()
        page.pets.click_back_btn()
        page.login.logout()
        # Открываем объявление пользователем 2 и отправляем сообщение пользователю 1
        page.login.authorization(test_user_login, test_user_password)
        page.open_bottom_sheet()
        page.select_market_filter()
        page.user_open_ad(ad_name)
        page.market.checking_more_options_user()
        page.market.add_to_favorite()
        page.market.click_contact_seller_btn()

        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images()
        page.chats.check_send_attachment()
        message = page.chats.check_send_text()
        page.chats.back_from_chat_to_main()
        page.menu.open_chats()
        page.chats.open_market_tab()
        page.chats.click_i_am_interested()
        page.chats.open_item_by_name(ad_name)
        page.chats.check_message_in_chat(message)

        # page.login.logout()
        # Открываем объявление пользователем 1 и проверяем сообщение от пользователя 2
        # page.login.authorization()
        # page.menu.open_chats()
        # page.chats.check_market_message(message)
        # new_message = faker.text()
        # page.market.send_message(new_message)

