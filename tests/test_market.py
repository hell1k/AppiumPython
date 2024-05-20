import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Market")
class TestMarket:
    @allure.title("Создание, редактирование, удаление")
    @pytest.mark.smoke
    @pytest.mark.market
    def test_create_new_business(self, authorization):
        page = MainPage()
        page.profile.open_market()
        page.market.check_create_buttons()
        page.market.create_new_ad_stuff()
