import time
import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
class TestChannels:

    @allure.title("Создание нового приватного канала")
    @pytest.mark.smoke
    def test_create_new_private_channel(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.add_new_channel('private')
        page.channels.edit_channel(channel_name)

    @allure.title("Создание нового не приватного канала")
    @pytest.mark.smoke
    def test_create_new_channel(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.add_new_channel()
        page.channels.edit_channel(channel_name)

    @allure.step("Проверка элементов канала при редактировании")
    def test_checking_channels_elements(self, authorization):
        self.menu.open_channels()
        page = MainPage()
        channel_name = page.channels.open_or_create_channel()
        page.channels.click_edit_channel()
        page.channels.add_to_favorite()
        page.channels.checking_more_options()
        # page.channels.checking_chat_btn()
        # page.swipe_up(3)
        # page.channels.checking_invite_people_btn()
        # page.press_back()
        # page.channels.checking_members_on_map(channel_name)
        # page.press_back()
        # page.channels.checking_blocked_members()

    @allure.step("Проверка пользовательских элементов группы")
    def test_checking_user_items(self, authorization):
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
        page.channels.click_edit_group()
        page.channels.swipe_up(5)
        page.channels.delete_and_leave(channel_name)
