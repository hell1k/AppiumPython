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

    @allure.title("Создать публикацию рынка - транспорт MARKET - HOUSING")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_market_housing(self, authorization):
        page = MainPage()
        page.profile.open_market()
        page.market.click_plus_new_market()
        page.market.select_housing_type_ad()
        page.market.click_create()
        ad_name = page.market.create_new_ad_housing()
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

    @allure.title("Создать публикацию канала CHANNELS")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_channel(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(channel_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Создать публикацию JOB")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_job(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.check_business_item_availability()
        page.business.click_back_btn()
        page.profile.click_jobs()
        position_name = page.jobs.create_new_jobs()
        page.click_back_btn()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(position_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Создать публикацию PETS")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_pets(self, authorization):
        page = MainPage()
        page.profile.open_pets()
        page.pets.add_new_pet_btn()
        page.pets.click_ok()
        page.pets.add_photo()
        pet_name = page.pets.add_new_pet()
        page.click_back_btn()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(pet_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Создать публикацию PLACE")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_place(self, authorization):
        page = MainPage()
        page.profile.open_places()
        page.place.click_add_new_place()
        place_name = page.place.create_new_place()
        page.click_back_btn()
        start_coins = page.ticker.get_mfc_balance()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.select_item_for_posting(place_name)
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_balance(start_coins, cost)
        page.ticker.check_purchase_history(cost)

    @allure.title("Проверить фильтры Ticker Filters")
    @pytest.mark.smoke
    @pytest.mark.ticker
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_place(self, authorization):
        page = MainPage()
        page.menu.open_search()
        page.ticker.click_ticker_option()
        page.ticker.click_ticker_filters()
        page.ticker.check_ticker_filters()

