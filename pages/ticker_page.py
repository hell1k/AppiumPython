import random
import time

import allure
from faker import Faker
from common.permission import Permission
from pages.base_page import BasePage
from common.menu import Menu
from common.photo import Photo
from pages.profile_page import ProfilePage
from tests.config import *

faker = Faker()


class TickerPage(BasePage):
    menu = Menu()
    photo = Photo()
    profile = ProfilePage()

    ticker_options = "com.yapmap.yapmap:id/ticker_options_image_view"
    create_a_posting = '//*[@text="Create a Posting"]'
    ticker_filters = '//*[@text="Ticker Filters"]'
    cancel_button = "com.yapmap.yapmap:id/cancel_button"
    send_message_field = "com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"
    add_file_btn = "com.yapmap.yapmap:id/attach_file_layout"
    post_button = "com.yapmap.yapmap:id/post_button"
    radius_ruler = "com.yapmap.yapmap:id/radius_ruler_view"
    rounds_ruler = "com.yapmap.yapmap:id/rounds_ruler_view"
    interval_between_rounds_ruler = "com.yapmap.yapmap:id/interval_between_rounds_ruler_view"
    attachment_delete = "com.yapmap.yapmap:id/attachment_delete_click_view"
    cost_text = "com.yapmap.yapmap:id/cost_text_view"
    balance_coins = "com.yapmap.yapmap:id/dozen_count_text_view"
    last_purchased_price_text = '//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[3]'
    last_purchased_description = '//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[2]'
    more_options = '//*[@resource-id="com.yapmap.yapmap:id/options_image_view"]'

    personal_ads_switch = '//*[@text="Personal ads"]/..'
    groups_switch = '//*[@text="Groups"]/..'
    channels_switch = '//*[@text="Channels"]/..'
    market_ads_selection = '//*[@text="Market ads"]/..'
    events_selection = '//*[@text="Events"]/..'
    local_deals_selection = '//*[@text="Local deals"]/..'
    pets_selection = '//*[@text="Pets"]/..'
    places_selection = '//*[@text="Places"]/..'
    jobs_selection = '//*[@text="Jobs"]/..'

    last_post_ticker = '//*[@resource-id="com.yapmap.yapmap:id/ticker_recycler_view"]/android.view.ViewGroup[8]/android.widget.FrameLayout[1]'

    def click_ticker_option(self):
        self.click(self.ticker_options, 'Кнопка ...')

    def click_create_a_posting(self):
        self.click(self.create_a_posting, 'Кнопка Create a Posting')

    def click_ticker_filters(self):
        self.click(self.ticker_filters, 'Кнопка Ticker Filters')

    def click_cancel_button(self):
        self.click(self.cancel_button, 'Кнопка Cancel')

    def click_add_file(self):
        self.click(self.add_file_btn, 'Кнопка Add file')

    def click_pay_now(self):
        input_string = self.get_text(self.cost_text)
        cost = float(input_string.replace('COST: ', ''))
        self.wait_element(self.post_button)
        self.click(self.post_button, 'Кнопка Pay Now')
        self.wait_a_second()
        return cost

    def click_delete_attachment(self):
        self.click(self.attachment_delete, 'Кнопка Delete attachment')

    @allure.step("Заполнить поле Send message")
    def set_message(self):
        self.swipe_to_element(self.send_message_field)
        message = faker.text()
        self.set_text(self.send_message_field, message)
        return message

    @allure.step("Отправить attachment")
    def check_send_attachment(self):
        self.swipe_to_element(self.add_file_btn)
        self.wait_a_second()
        self.click_add_file()
        self.wait_a_second()
        self.click(self.d(resourceId="com.yapmap.yapmap:id/button", text="Select from gallery"))
        self.wait_a_second()
        self.photo.upload_picture()
        self.wait_a_second()
        self.wait_a_second()
        self.wait_text('Attach a file')
        self.click_delete_attachment()
        self.wait_a_second()
        self.click_add_file()
        self.click(self.d(resourceId="com.yapmap.yapmap:id/button", text="Select from files"))
        self.click(self.get_random_element_gallery(
            '//*[@resource-id="com.google.android.documentsui:id/dir_list"]/android.widget.LinearLayout'))

    def swipe_ruler(self, locator):
        center = self.get_element(locator).center()
        fx, fy = center
        ty = fy
        tx = fx - 80
        self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)

    @allure.step("Установить ползунки")
    def set_rulers(self):
        random_number = random.randint(1, 3)
        self.swipe_to_element(self.radius_ruler)
        for count in range(1, random_number + 1):
            self.swipe_ruler(self.radius_ruler)
        self.swipe_to_element(self.rounds_ruler)
        for count in range(1, random_number + 1):
            self.swipe_ruler(self.rounds_ruler)
        self.swipe_to_element(self.interval_between_rounds_ruler)
        for count in range(1, random_number + 1):
            self.swipe_ruler(self.interval_between_rounds_ruler)
        self.get_screen()

    def click_more_options(self):
        self.click(self.more_options, 'Кнопка ... (more options)')

    def check_balance(self, start_coins, cost):
        mfc_balance = self.get_mfc_balance()
        count_cost = round(start_coins - mfc_balance, 2)
        assert count_cost == cost, f'Разница начального баланса {start_coins} и текущего баланса {mfc_balance} вышла {count_cost}, что не равно стоимости публикации {cost}'

    def get_mfc_balance(self):
        self.menu.open_profile()
        self.swipe_down_to_element(self.balance_coins)
        mfc_balance = self.get_text(self.balance_coins)
        new_string = mfc_balance.replace(",", "")
        mfc_balance = float(new_string)
        return mfc_balance

    def check_purchase_history(self, cost):
        self.profile.open_purchase_history()
        amount_text = self.get_text(self.last_purchased_price_text)
        amount = float(amount_text.replace("-", ""))
        was_paid_text = self.get_text(self.last_purchased_description)
        was_paid_step = was_paid_text.replace("You have purchased ticker. ", "")
        was_paid = float(was_paid_step.replace(" MFC was paid.", ""))
        assert amount == was_paid, f'Число в описании {was_paid} не совпадает с числом в стоимости {amount}'
        assert amount == cost, f'Число при оформлении {cost} не равно числу в стоимости {amount}'

    def select_item_for_posting(self, item_name):
        self.swipe_to_element(f'//*[@text="{item_name}"]')
        self.click(f'//*[@text="{item_name}"]')

    def check_selectors(self):
        self.click_more_options()
        self.click('//*[@text="Cancel"]')
        self.click_more_options()
        self.click('//*[@text="Unselect all"]')
        self.click(self.get_random_element('//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout'))
        self.swipe_to_element('//*[@text="Other"]')
        self.click(self.get_random_element('//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout'))
        self.click_more_options()
        self.click('//*[@text="Select all"]')
        self.press_back()

    def check_ticker_filters(self):
        self.wait_text('Ticker Filters')
        self.click(self.personal_ads_switch)
        self.click(self.groups_switch)
        self.click(self.channels_switch)

        self.click(self.market_ads_selection)
        self.wait_text('Stuff')
        self.wait_text('Housing')
        self.wait_text('Transportation')
        self.press_back()

        self.click(self.events_selection)
        self.wait_text('Events')
        self.click_more_options()
        self.click('//*[@text="Cancel"]')
        self.click_more_options()
        self.click('//*[@text="Unselect all"]')
        self.click(self.get_random_element('//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout'))
        self.swipe_to_element('//*[@text="Workshop"]')
        self.click(self.get_random_element('//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout'))
        self.click_more_options()
        self.click('//*[@text="Select all"]')
        self.press_back()

        self.click(self.local_deals_selection)
        self.wait_text('Businesses')
        self.check_selectors()

        self.click(self.pets_selection)
        self.wait_text('Pets')
        self.check_selectors()

        self.click(self.places_selection)
        self.wait_text('Places')
        self.check_selectors()

        self.click(self.jobs_selection)
        self.wait_text('Profession type')
        self.check_selectors()

    def check_post(self, name, message):
        self.click(self.last_post_ticker)
        self.wait_text(name)
        self.wait_text(message)

    def check_post_profile_ticker(self, message):
        time.sleep(120)
        self.click(self.last_post_ticker)
        self.wait_text(message)
