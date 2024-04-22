import time
import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
class TestChannels:

    @allure.title("Создание нового приватного канала")
    @pytest.mark.smoke
    def test_create_new_private_channel(self, login):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.add_new_channel('private')
        page.channels.edit_channel(channel_name)

    @allure.title("Создание нового не приватного канала")
    @pytest.mark.smoke
    def test_create_new_channel(self, login):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.add_new_channel()
        page.channels.edit_channel(channel_name)

    @allure.step("Проверка элементов канала при редактировании")
    def test_checking_channels_elements(self, login):
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

    @allure.step("Проверка пользовательских элементов канала")
    def test_checking_user_items(self, login):
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

    @allure.step("Взаимодействие с группой участником группы")
    def test_channels_participant(self, login):
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

    # @allure.step("Очистка чата администратором")
    # def test_clear_chat(self, login):
    #     page = MainPage()
    #     page.menu.open_channels()
    #     channel_name = page.channels.open_or_create_channel()
    #     page.press_back()
    #     page.login.logout()
    #     page.login.authorization(test_user_login, test_user_password)
    #     page.menu.open_channels()
    #     page.channels.join_a_channel(channel_name)
    #     page.channels.click_chat_icon()
    #     new_message = faker.text()
    #     page.channels.send_message(new_message)
    #     page.press_back()
    #     page.press_back()
    #     page.login.logout()
    #     page.login.authorization()
    #     page.menu.open_groups()
    #     page.channels.open_group(channel_name)
    #     page.channels.click_edit_channel()
    #     page.swipe_up(5)
    #     page.channels.clear_chat_history()
    #     page.press_back()
    #     page.login.logout()
    #     page.login.authorization(test_user_login, test_user_password)
    #     page.menu.open_groups()
    #     page.channels.open_group(channel_name)
    #     page.channels.checking_empty_chat()

