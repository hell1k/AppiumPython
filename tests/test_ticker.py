import allure
import pytest
from pages.ticker_page import TickerPage
from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Ticker")
class TestTicker:
    @allure.title("Создать публикацию профиля PROFILE")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_profile(self, authorization):
        page = MainPage()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Создать публикацию группы GROUPS")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_group(self, authorization):
        page = MainPage()
        page.menu.open_groups()
        group_name = page.groups.add_new_group()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(group_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Создать публикацию ивента EVENTS")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_event(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event()
        page.click_back_btn()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(event_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Создать публикацию бизнеса BUSINESS")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_business(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.clear_business()
        business_name = page.business.add_new_business()
        page.click_back_btn()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(business_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Создать публикацию рынка - транспорт MARKET - TRANSPORTATION")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_market_transport(self, authorization):
        page = MainPage()
        page.profile.open_market()
        ad_name = page.market.create_market_transport()
        page.click_back_btn()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(ad_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Создать публикацию рынка - транспорт MARKET - STUFF")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_market_transport(self, authorization):
        page = MainPage()
        page.profile.open_market()

        ad_name = page.market.create_market_stuff()

        page.click_back_btn()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(ad_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)
