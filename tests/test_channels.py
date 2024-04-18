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

