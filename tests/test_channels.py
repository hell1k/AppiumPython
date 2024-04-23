import time
import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Канал")
class TestChannels:

    @allure.title("Создание нового приватного канала")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_create_new_private(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.add_new_channel('private')
        page.channels.edit_channel(channel_name)

    @allure.title("Создание нового не приватного канала")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_create_new(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.add_new_channel()
        page.channels.edit_channel(channel_name)

    @allure.title("Проверка элементов канала при редактировании")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_checking_elements(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.open_or_create_channel()
        page.channels.click_edit_channel()
        page.channels.add_to_favorite()
        page.channels.checking_more_options()
        page.swipe_up(3)
        page.channels.checking_add_members_btn()
        page.press_back()
        # page.channels.checking_members_on_map(channel_name)
        # page.press_back()
        page.channels.checking_blocked_members()

    @allure.title("Проверка элементов приватного канала при редактировании")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_private_checking_elements(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.open_or_create_private_channel()
        page.channels.click_edit_channel()
        page.channels.add_to_favorite()
        page.channels.checking_more_options()
        page.channels.checking_more_options_private()
        page.swipe_up(3)
        page.channels.checking_add_members_btn()
        page.press_back()
        # page.channels.checking_members_on_map(channel_name)
        # page.press_back()
        page.channels.checking_blocked_members()

    @allure.title("Проверка пользовательских элементов канала")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_checking_user_items(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.open_or_create_channel()
        page.channels.click_edit_channel()
        page.channels.swipe_up(3)
        page.channels.add_admin()
        page.channels.press_back()
        page.channels.edit_members()
        page.channels.press_back()
        page.channels.press_back()
        page.channels.send_message(faker.text())
        page.channels.click_edit_channel()
        page.channels.swipe_up(3)
        page.channels.delete_and_leave(channel_name)

    @allure.title("Взаимодействие с группой участником канала")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_participant(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.open_or_create_channel()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_channels()
        page.channels.join_a_channel(channel_name)
        page.swipe_up(3)
        page.channels.checking_report_channel_btn()
        page.press_back()
        page.channels.leave_channel(channel_name)

    @allure.title("Очистка чата администратором")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_clear_chat(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.open_or_create_channel()
        new_message = faker.text()
        page.channels.send_message(new_message)
        page.channels.click_edit_channel()
        page.swipe_up(5)
        page.channels.clear_chat_history()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_channels()
        page.channels.open_channel(channel_name)
        page.channels.checking_empty_chat()
