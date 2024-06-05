import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Chats")
class TestChats:
    @allure.title("Проверка добавления и удаления стикер пака")
    @pytest.mark.smoke
    @pytest.mark.chats
    def test_add_and_del_sticker_pack(self):
        page = MainPage()
        page.login.registration()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        new_message = faker.text()
        page.channels.send_message(new_message)
        page.chats.add_sticker_pack()
        page.chats.check_send_sticker()
        page.chats.del_sticker_pack()


    # @allure.title("Проверка отправки всех типов медиа в чат business")
    # @pytest.mark.smoke
    # @pytest.mark.business
    # @pytest.mark.chat
    # def test_chat_business(self, authorization):
    #     page = MainPage()
    #     page.profile.open_business()
    #     page.business.clear_business()
    #     business_name = page.business.add_new_business()
    #     page.wait_text(business_name)
    #     page.business.user_open_business(business_name)
    #     page.business.user_check_business()
    #     page.chats.test_chat()
    #     page.chats.check_send_emoji()
    #     page.chats.check_send_sticker()
    #     page.chats.check_send_images()
    #     page.chats.check_send_images_from_camera()
    #     page.chats.check_send_attachment()

    @allure.title("Проверка отправки всех типов медиа в чат channels и очистка чата")
    @pytest.mark.smoke
    @pytest.mark.channels
    @pytest.mark.chats
    def test_channels_chat(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        new_message = faker.text()
        page.channels.send_message(new_message)
        page.chats.check_send_emoji()
        page.chats.check_send_sticker()
        page.chats.check_send_images()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_attachment()
        page.channels.click_edit_channel()
        page.swipe_to_element(page.channels.clear_chat_history_btn)
        page.channels.clear_chat_history()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_channels()
        page.channels.open_channel(channel_name)
        page.channels.checking_empty_chat()

    @allure.title("Проверка отправки всех типов медиа в чат groups и очистка чата")
    @pytest.mark.smoke
    @pytest.mark.groups
    @pytest.mark.chats
    def test_groups_chat(self, authorization):
        page = MainPage()
        page.menu.open_groups()
        group_name = page.groups.add_new_group()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_groups()
        page.groups.join_an_open_group(group_name)
        page.groups.click_chat_icon()
        new_message = faker.text()
        page.groups.send_message(new_message)
        page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_attachment()
        page.press_back()
        page.press_back()
        page.login.logout()
        page.login.authorization()
        page.menu.open_groups()
        page.groups.open_an_open_group(group_name)
        page.groups.click_edit_group()
        page.groups.clear_chat_history()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_groups()
        page.groups.open_an_open_group(group_name)
        page.groups.checking_empty_chat()

    @allure.title("Проверка отправки всех типов медиа в чат events и очистка чата")
    @pytest.mark.smoke
    @pytest.mark.events
    @pytest.mark.chats
    def test_event_chat(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event()
        page.events.user_open_event(event_name)
        page.events.checking_chat_btn()
        new_message = faker.text()
        page.events.send_message(new_message)
        page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_attachment()
        page.events.click_edit()
        page.swipe_to_element(page.events.clear_chat_history_btn)
        page.events.clear_chat_history()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.events.user_open_event(event_name)
        page.events.checking_empty_chat()

    @allure.title("Взаимодействие с пользователем")
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
        message = page.chats.check_send_text()
        page.chats.check_send_emoji()
        page.chats.check_send_sticker()
        page.chats.check_send_images()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_attachment()
        page.chats.back_from_chat_to_main()
        page.login.logout()
        # Открываем объявление пользователем 1 и проверяем сообщение от пользователя 2
        page.login.authorization()
        page.menu.open_chats()
        page.chats.check_market_message(message)
        new_message = faker.text()
        page.market.send_message(new_message)
