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
        ad_name = page.market.create_new_ad_stuff()
        page.market.open_market(ad_name)
        page.market.checking_more_options()
        page.market.open_market(ad_name)
        new_ad_name = page.market.edit_ad()
        page.market.open_market(new_ad_name)
        page.market.delete_ad(new_ad_name)
