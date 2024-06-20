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
    @pytest.mark.lenta
    @pytest.mark.login_marker("yapmap.tester+market@yandex.ru")
    def test_create_a_posting_profile(self, authorization):
        page = MainPage()
        start_coins = page.ticker.get_mfc_balance()
        page.ticker.click_ticker_option()
        page.ticker.click_create_a_posting()
        page.ticker.set_rulers()
        page.ticker.set_message()
        page.ticker.check_send_attachment()
        page.swipe_up()
        cost = page.ticker.click_pay_now()
        page.ticker.check_purchase_history(start_coins, cost)
        print('test')

