import random

import allure
import faker
from faker import Faker
from common.menu import Menu
from common.permission import Permission
from pages.base_page import BasePage
from tests.config import *


class PlacesPage(BasePage):
    menu = Menu()
    faker = Faker()

    plus_btn = 'com.yapmap.yapmap:id/action_create'
    create_btn = 'com.yapmap.yapmap:id/create_button'
    cancel_button = "com.yapmap.yapmap:id/cancel_button"
    create_button = "com.yapmap.yapmap:id/create_button"
    add_a_place_btn = "com.yapmap.yapmap:id/join_button"
    around_tab = '//*[@content-desc="Around"]'
    places_tab = '//*[@content-desc="Places"]'
    search_field = "com.yapmap.yapmap:id/search_src_text"

    add_photo_btn = 'com.yapmap.yapmap:id/photos_field_add_photo_text_view'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/avatar_layout"]/android.widget.FrameLayout[1]'
    title_field = "com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"
    done_photo = "com.yapmap.yapmap:id/action_done"

    place_type = '//*[@text="Place type"]/..'
    location = '//*[@text="Location"]/..'
    types = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout'
    type_address_field = "com.yapmap.yapmap:id/auto_complete_text_view"
    address_popup = "android:id/text1"
    map_plus_btn = '//*[@resource-id="com.yapmap.yapmap:id/floating_action_button"]'
    description_field = "com.yapmap.yapmap:id/description_edit_text"

    more_options = "com.yapmap.yapmap:id/action_show_option_menu"
    back_btn = '//*[@content-desc="Back"]'
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    share_text = '//*[@resource-id="android:id/content_preview_text" and contains(@text, "Hey! Look at the place")]'
    qr_code = 'com.yapmap.yapmap:id/qr_code_image_view'
    input_edit_text = '//*[@resource-id="com.yapmap.yapmap:id/input_edit_text"]'

    like_button = "com.yapmap.yapmap:id/like_button"
    dislike_button = "com.yapmap.yapmap:id/dislike_button"
    rates_count_text_view = "com.yapmap.yapmap:id/rates_count_text_view"

    group_chat_btn = "com.yapmap.yapmap:id/group_chat_text_view"
    back_btn_2 = '//androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'
    send_message_btn = "com.yapmap.yapmap:id/contact_seller_text_view"
    message_field = 'com.yapmap.yapmap:id/input_edit_text'
    send_message_chat_btn = 'com.yapmap.yapmap:id/send_button_image_view'
    pop_up_ok_btn = "com.yapmap.yapmap:id/ok_button"

    add_address_btn = 'com.yapmap.yapmap:id/address_location_field'
    address_location = 'com.yapmap.yapmap:id/activity_content_container'
    address_apply_btn = 'com.yapmap.yapmap:id/floating_action_button'

    title = "com.yapmap.yapmap:id/title_text_view"
    share_title = '//*[(@resource-id="android:id/title" and @text="Share") or @resource-id="android:id/sem_chooser_share_live_icon"]'

    @allure.step("Клик по кнопке Назад")
    def click_back_btn(self):
        self.click(self.back_btn, "кнопка Назад")

    @allure.step("Нажатие кнопки Добавить новое место")
    def click_add_new_place(self):
        self.click(self.plus_btn, 'кнопка +')

    @allure.step("Добавление нового фото")
    def upload_new_photo(self):
        self.click(self.add_photo_btn, 'add photo')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.take_a_photo()
        self.click(self.done_photo, 'кнопка Done')
        self.wait_a_second()

    @allure.step("create_new_place")
    def create_new_place(self):
        self.upload_new_photo()
        place_name = self.set_name()
        self.swipe_to_element(self.place_type)
        self.click(self.place_type, 'пункт Place type')
        self.select_random()

        self.swipe_to_element(self.location)
        self.click(self.location, 'пункт Location')
        self.set_address()
        # self.select_address()

        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_1000)

        self.swipe_to_element(self.create_button)
        self.click(self.create_button, 'кнопка ADD A PLACE')

        self.wait_text('Places to Visit')
        self.swipe_down()
        self.wait_a_second()
        self.wait_text(place_name)
        return place_name

    @allure.step("click_tab_around")
    def click_tab_around(self):
        self.click(self.around_tab, 'tab Around')

    @allure.step("click_tab_places")
    def click_tab_places(self):
        self.click(self.places_tab, 'tab Places')

    @allure.step("Переход в доп опции группы '{option_name}'")
    def open_more_options(self, option_name):
        self.click(self.more_options, "меню группы")
        self.click(f'//*[@text="{option_name}"]', option_name)

    @allure.step("Проверка меню ... в шапке")
    def checking_more_options(self):
        self.wait_a_moment()
        self.open_more_options("Edit")
        self.wait_text('Editing')
        self.click_back_btn()
        self.wait_a_moment()
        self.open_more_options("Share")
        self.wait_element(self.share_title)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Chat")
        assert self.get_text(self.input_edit_text) == 'Type message…', 'Поле ввода с текстом Type message… не найдено'
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Delete")
        self.wait_text('Delete')
        self.click(self.cancel_button, 'кнопка Cancel')
        self.wait_hidden_element(self.cancel_button)
        self.wait_a_moment()
        self.open_more_options("Cancel")
        self.wait_hidden_element(self.cancel_button)

    @allure.step("Проверка меню ... в шапке")
    def checking_more_options_user_place(self, place_name):
        self.wait_a_moment()
        self.open_more_options("Share")
        self.wait_element(self.share_text)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Chat")
        assert self.get_text(self.title) == place_name
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Complain")
        self.wait_text('Choose a reason')
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Cancel")
        self.wait_hidden_element(self.cancel_button)

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.wait_a_second()
        self.click(self.add_to_favorites_btn, "кнопка добавления в избранное")
        self.wait_a_second()

    @allure.step("Открыть Place")
    def open_place(self, place_name):
        self.wait_a_second()
        self.swipe_down_to_element(f'//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout//*[@text="{place_name}"]')
        self.click(
            f'//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout//*[@text="{place_name}"]')

    @allure.step("Заполнение поля Name")
    def set_name(self):
        ad_name = 'Test Place_' + str(random.randint(0, 999999999))
        self.set_text(self.title_field, ad_name, "Name")
        return ad_name

    @allure.step("Выбрать адрес")
    def set_address(self, city_name='Novosibirsk'):
        self.wait_text('Choose location')
        self.set_text(self.type_address_field, city_name)
        self.click(self.address_popup, 'адрес из всплывашки')
        # self.coordinate_click(self.d.window_size()[0] / 2, self.d.window_size()[1] / 2)
        self.click(self.map_plus_btn, 'кнопка + на карте')

    @allure.step("Добавление адреса")
    def select_address(self):
        # self.swipe_to_element(self.add_address_btn)
        # self.click(self.add_address_btn, "add address")
        location_coordinate = self.get_element(self.address_location).center()
        self.d.click(location_coordinate[0], location_coordinate[1])
        self.click(self.address_apply_btn, "добавить выбранный адрес")

    @allure.step("Выбор случайного типа")
    def select_random(self):
        self.wait_element(self.types)
        self.click(self.get_random_element(self.types), "рандомный тип")
        self.wait_a_moment()

    @allure.step("Нажатие кнопки 'Like")
    def check_like_and_dislike_btn(self):
        count = int(self.get_text(self.rates_count_text_view))
        self.click(self.like_button)
        assert int(self.get_text(self.rates_count_text_view)) == count + 1
        self.click(self.like_button)
        assert int(self.get_text(self.rates_count_text_view)) == count

        self.click(self.dislike_button)
        assert int(self.get_text(self.rates_count_text_view)) == count + 1
        self.click(self.dislike_button)
        assert int(self.get_text(self.rates_count_text_view)) == count

    @allure.step("Нажатие кнопки 'Груповой чат")
    def click_group_chat_btn(self, place_name):
        self.swipe_to_element(self.group_chat_btn)
        self.click(self.group_chat_btn, 'кнопка Group chat')
        # assert self.get_text(self.input_edit_text) == 'Type message…', 'Поле ввода с текстом Type message… не найдено'
        assert self.get_text(self.title) == place_name

    @allure.step("Проверяем чат")
    def test_chat(self):
        message = faker.text()
        self.send_message(message)
        self.swipe_up()
        self.wait_text(message)
        self.click(self.back_btn_2)
        return message

    @allure.step("Отправка в чат сообщения '{message}'")
    def send_message(self, message):
        self.set_text(self.message_field, message, "сообщение")
        self.click(self.send_message_chat_btn, "кнопка отправки сообщения")
        self.wait_a_second()
        self.wait_a_second()
        self.swipe_up()
        self.wait_text(message)

    @allure.step("Добавить фото")
    def add_photo_without_permissions(self):
        self.click(self.add_photo_btn, 'кнопка Add photos')
        self.click(self.image_loader, "добавление нового фото")
        self.take_a_photo()
        self.wait_a_second()
        self.click(self.done_photo, 'кнопка Done')

    @allure.step("Редактирование Place")
    def edit_place(self):
        self.click(self.more_options, 'кнопка ... в верхнем правом углу')
        self.click('//*[@text="Edit"]')
        self.add_photo_without_permissions()
        place_name = self.set_name()
        self.swipe_to_element(self.place_type)
        self.click(self.place_type, 'пункт Place type')
        self.select_random()

        self.swipe_to_element(self.location)
        self.click(self.location, 'пункт Location')
        self.set_address()

        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_1000_2)

        self.swipe_to_element(self.create_button)
        self.click(self.create_button, 'кнопка EDIT')
        self.wait_element(self.add_to_favorites_btn)
        self.click_back_btn()
        self.wait_text('Places to Visit')
        self.swipe_down()
        self.wait_a_second()
        self.wait_text(place_name)
        return place_name

    @allure.step("Удалить Place")
    def delete_ad(self, place_name):
        self.click(self.more_options, 'кнопка ... в верхнем правом углу')
        self.click('//*[@text="Delete"]')
        self.click(self.pop_up_ok_btn, 'кнопка ОК на popup')
        self.swipe_down()
        self.wait_a_second()
        self.d(resourceId='com.yapmap.yapmap:id/recycler_view').child(text=place_name).wait_gone(10)

    @allure.step("Проверка наличия сообщения в чате")
    def check_chat_msg(self, message):
        self.wait_text(message)

    @allure.step("Поиск place по названию")
    def search_place(self, place_name):
        self.set_text(self.search_field, place_name)
