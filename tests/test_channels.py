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
        channel_name = self.channels.add_new_channel('private')
        self.channel.edit_group(channel_name)

