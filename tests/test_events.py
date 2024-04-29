import time
import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Events")
class TestEvents:

    @allure.title("Создание нового приватного события")
    @pytest.mark.smoke
    @pytest.mark.events
    def test_events_create_new_private(self, login):
        page = MainPage()
        page.profile.open_events()
        page.events.add_new_event('private')

