import random
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
        self.wait_element(self.post_button)
        self.click(self.post_button, 'Кнопка Pay Now')
        cost = int(self.get_text(self.cost_text))
        return cost

    def click_delete_attachment(self):
        self.click(self.attachment_delete, 'Кнопка Delete attachment')

    @allure.step("Заполнить поле Send message")
    def set_message(self):
        self.swipe_to_element(self.send_message_field)
        message = faker.text()
        self.set_text(self.send_message_field, message)

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
        self.click(self.get_random_element(
            '//*[@resource-id="com.google.android.documentsui:id/dir_list"]/android.widget.LinearLayout'))

    def swipe_ruler(self, locator):
        center = self.get_element(locator).center()
        fx, fy = center
        ty = fy
        tx = fx - 80
        self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)

    @allure.step("Установить ползунки")
    def set_rulers(self):
        self.swipe_to_element(self.radius_ruler)
        self.swipe_ruler(self.radius_ruler)
        self.swipe_to_element(self.rounds_ruler)
        self.swipe_ruler(self.rounds_ruler)
        self.swipe_to_element(self.interval_between_rounds_ruler)
        self.swipe_ruler(self.interval_between_rounds_ruler)
        self.get_screen()

    def check_purchase_history(self):
        self.menu.open_profile()
        self.profile.open_purchase_history()


