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
    @pytest.mark.demo
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
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        page.channels.click_edit_channel()
        page.channels.checking_channel_name_limit(channel_name)
        page.channels.add_to_favorite()
        page.channels.checking_more_options()
        page.swipe_to_element(page.channels.add_members_btn)
        page.channels.checking_add_members_btn()
        page.press_back()
        page.channels.checking_blocked_members()

    @allure.title("Проверка элементов приватного канала при редактировании")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_private_checking_elements(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.open_or_create_private_channel()
        page.channels.click_edit_channel()
        page.channels.checking_channel_name_limit(channel_name)
        page.channels.add_to_favorite()
        page.channels.checking_more_options()
        page.channels.checking_more_options_private()
        page.swipe_to_element(page.channels.add_members_btn)
        page.channels.checking_add_members_btn()
        page.press_back()
        page.channels.checking_blocked_members()

    @allure.title("Проверка пользовательских элементов канала")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_checking_user_items(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        page.channels.click_edit_channel()
        page.channels.add_admin()
        page.channels.press_back()
        page.channels.edit_members()
        page.channels.press_back()
        page.channels.press_back()
        page.channels.send_message(faker.text())
        page.channels.click_edit_channel()
        page.swipe_to_element(page.channels.leave_channel_btn)
        page.channels.delete_and_leave(channel_name)

    @allure.title("Взаимодействие с группой участником канала")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_participant(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_channels()
        page.channels.join_a_channel(channel_name)
        page.swipe_to_element(page.channels.leave_channel_btn)
        page.channels.checking_report_channel_btn()
        page.press_back()
        page.channels.leave_channel(channel_name)

    @allure.title("Очистка чата администратором")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_clear_chat(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        new_message = faker.text()
        page.channels.send_message(new_message)
        page.channels.click_edit_channel()
        page.swipe_to_element(page.channels.clear_chat_history_btn)
        page.channels.clear_chat_history()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_channels()
        page.channels.open_channel(channel_name)
        page.channels.checking_empty_chat()

    @allure.title("Проверка комментария к сообщению в канале")
    @pytest.mark.smoke
    @pytest.mark.channels
    def test_channels_comment(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        new_message = faker.text()
        page.channels.send_message(new_message)
        comment = page.channels.checking_channel_comment()
        page.press_back()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_channels()
        page.channels.open_channel(channel_name)
        page.channels.checking_channel_comment_member(comment)

