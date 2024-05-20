import random

import allure
import faker
from faker import Faker
from common.menu import Menu
from common.permission import Permission
from pages.base_page import BasePage
from tests.config import *


class MarketPage(BasePage):
    menu = Menu()
    faker = Faker()

    plus_market_btn = 'com.yapmap.yapmap:id/action_create'
    create_btn = 'com.yapmap.yapmap:id/create_button'
    cancel_button = "com.yapmap.yapmap:id/cancel_button"
    create_button = "com.yapmap.yapmap:id/create_button"
    type_switch_sale_rent = "com.yapmap.yapmap:id/type_switch"
    transportation_type = "com.yapmap.yapmap:id/transportation_text_view"
    stuff_type = "com.yapmap.yapmap:id/item_text_view"
    housing_type = "com.yapmap.yapmap:id/housing_text_view"
    add_photo_btn = 'com.yapmap.yapmap:id/photos_field_add_photo_text_view'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/avatar_layout"]/android.widget.FrameLayout[1]'
    title_field = "com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"
    done_photo = "com.yapmap.yapmap:id/action_done"
    category_selection = '//*[@text="Category"]/..'
    type_selection = '//*[@text="Type"]/..'
    zip_selector = '//*[@text="ZIP"]/..'
    price_selector = '//*[@text="Price"]/..'
    location_selector = '//*[@text="Location"]/..'
    currency_selector = '//*[@text="Currency"]/..'
    shipping_available_switch = '//*[@text="Shipping available"]/..'
    exchange_is_possible_switch = '//*[@text="Exchange is possible"]/..'
    bargaining_is_possible_switch = '//*[@text="Bargaining is possible"]/..'
    types = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout'
    type_address_field = "com.yapmap.yapmap:id/auto_complete_text_view"
    address_popup = '//*[@text="Novosibirsk, Novosibirsk Oblast, Russia"]'
    map_plus_btn = '//*[@resource-id="com.yapmap.yapmap:id/floating_action_button"]'
    edit_text_view = "com.yapmap.yapmap:id/edit_text_view"
    description_field = '//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"]'
    post_button = '//*[@resource-id="com.yapmap.yapmap:id/post_button"]'

    def click_back_btn(self):
        self.click(self.d(description="Back"), "кнопка Назад")

    def click_plus_new_market(self):
        self.click(self.plus_market_btn, "кнопка + создания новой сущности Market")

    def click_create(self):
        self.click(self.create_btn, "кнопка Create")

    def check_create_buttons(self):
        self.click_plus_new_market()
        self.wait_text('Create an ad')
        self.click_back_btn()
        self.click_create()
        self.wait_text('Create an ad')
        self.click(self.cancel_button)

    @allure.step("Выбор случайного типа")
    def select_random_type_ad(self):
        random_type = random.randrange(1, 3)
        if random_type == 1:
            self.click(self.transportation_type)
        if random_type == 2:
            self.click(self.stuff_type)
        if random_type == 3:
            self.click(self.housing_type)
        random_type = random.randrange(1, 2)
        if random_type == 1:
            self.click(self.type_switch_sale_rent)
        else:
            pass

    @allure.step("Добавление нового фото")
    def upload_new_photo(self):
        self.click(self.add_photo_btn, 'add photo')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.click(self.done_photo)
        self.wait_a_second()

    @allure.step("Заполнение поля Advertisement name")
    def set_ad_name(self):
        self.swipe_to_element(self.title_field)
        self.set_text(self.title_field, self.faker.company(), "Advertisement name")

    @allure.step("Выбор случайного типа")
    def select_random(self):
        self.wait_element(self.types)
        self.click(self.get_random_element(self.types), "рандомный тип")
        self.wait_a_moment()

    @allure.step("Выбрать адрес")
    def set_address(self, city_name='Novosibirsk'):
        self.wait_text('Choose location')
        self.set_text(self.type_address_field, city_name)
        self.click(self.address_popup, 'адрес из всплывашки')
        self.click(self.map_plus_btn, 'кнопка + на карте')

    @allure.step("Создание нового Ad")
    def create_new_ad(self):
        self.click_create()
        self.select_random_type_ad()
        self.click_create()
        self.upload_new_photo()
        self.set_ad_name()
        self.swipe_to_element(self.category_selection)
        self.click(self.category_selection)
        self.select_random()
        self.swipe_to_element(self.type_selection)
        self.click(self.type_selection)
        self.select_random()
        print('test')

    @allure.step("Создание нового Ad Stuff")
    def create_new_ad_stuff(self):
        self.click_create()
        self.click_create()
        self.upload_new_photo()
        self.set_ad_name()
        self.swipe_to_element(self.category_selection)
        self.click(self.category_selection)
        self.select_random()

        try:
            self.click(self.type_selection)
            self.select_random()
        except:
            print('Нет раздела Type для выбранной категории')

        self.swipe_to_element(self.location_selector)
        self.click(self.location_selector)
        self.set_address()
        # self.click(self.zip_selector, 'ZIP')
        # random_zip = faker.zipcode()
        # self.set_text(self.edit_text_view, random_zip)

        self.swipe_to_element(self.price_selector)
        self.click(self.price_selector, 'Price')
        random_price = random.randrange(1, 10000)
        self.set_text(self.edit_text_view, random_price)

        self.swipe_to_element(self.type_selection)
        self.click(self.type_selection)
        self.select_random()

        self.click(self.shipping_available_switch)
        self.click(self.exchange_is_possible_switch)
        self.click(self.bargaining_is_possible_switch)

        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_1000)

        self.swipe_to_element(self.post_button)
        self.click(self.post_button)


        print('test')
