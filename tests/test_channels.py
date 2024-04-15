import time

import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
class TestChannels:

    @allure.title("Создание новой приватной группы")
    @pytest.mark.smoke
    def test_name(self, authorization):
        self.menu.open_channels()
        self.channels.add_new_channel()
        time.sleep(100)

