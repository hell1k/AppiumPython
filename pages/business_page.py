import random

import allure
from faker import Faker

from common.permission import Permission
from pages.base_page import BasePage
from common.menu import Menu
from tests.config import text_250

faker = Faker()


class BusinessPage(BasePage):
    menu = Menu()

    new_business_btn = '//*[@resource-id="com.yapmap.yapmap:id/action_create"]'
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/avatar_layout"]/android.widget.FrameLayout[1]'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    business_name_field = '//*[@resource-id="com.yapmap.yapmap:id/name_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    business_type = '//*[@resource-id="com.yapmap.yapmap:id/type_field"]//*[@resource-id="com.yapmap.yapmap:id/click_view"]'
    business_type_list = 'com.yapmap.yapmap:id/value_text_view'
    description = '//*[@resource-id="com.yapmap.yapmap:id/description_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    add_photo_btn = 'com.yapmap.yapmap:id/photos_field_add_photo_text_view'
    done_photo = 'com.yapmap.yapmap:id/action_done'
    add_address_btn = 'com.yapmap.yapmap:id/address_location_field'
    address_location = 'com.yapmap.yapmap:id/activity_content_container'
    address_apply_btn = 'com.yapmap.yapmap:id/floating_action_button'
    phone_field = '//*[@resource-id="com.yapmap.yapmap:id/phone_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    site_field = '//*[@resource-id="com.yapmap.yapmap:id/site_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    show_it_to_other_switch_btn = '//*[@resource-id="com.yapmap.yapmap:id/show_it_to_others_switch"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    create_new_business_btn = 'com.yapmap.yapmap:id/action_show_option_menu'
    ok_btn = 'com.yapmap.yapmap:id/ok_button'
    business_item = 'com.yapmap.yapmap:id/name_text_view'
    delete_btn = 'com.yapmap.yapmap:id/delete_button'
    save_btn = 'com.yapmap.yapmap:id/action_save'

    @allure.step("Добавление новой записи Business")
    def add_new_business(self):
        self.click_new_business_btn()
        self.upload_new_photo()
        business_name = self.set_name()
        self.set_business_type()
        self.set_description("Some description")
        self.swipe_up()
        self.add_new_photo()
        self.swipe_up()
        self.select_address()
        self.set_phone()
        self.set_site()
        self.swipe_up()
        self.click_show_it_to_other()
        self.click_create_btn()
        self.click(self.ok_btn, "кнопка OK")
        self.click(self.ok_btn, "кнопка OK")
        return business_name

    @allure.step("Клик по кнопке Create")
    def click_create_btn(self):
        self.click(self.create_new_business_btn, "кнопка Create")
        self.wait_text("New Business profile created")

    @allure.step("Клик по переключателю Show it to other")
    def click_show_it_to_other(self):
        self.click(self.show_it_to_other_switch_btn, "Show it to other")
        self.wait_a_second()

    @allure.step("Клик по кнопке создания новой сущности")
    def click_new_business_btn(self):
        self.click(self.new_business_btn, "кнопка добавления business")
        self.wait_text("New business")

    @allure.step("Добавление названия")
    def set_name(self):
        business_name = 'Test business_' + str(random.randint(0, 999999999))
        self.set_text(self.business_name_field, business_name, "поле Business name")
        return business_name

    @allure.step("Добавление Business type")
    def set_business_type(self):
        self.click(self.business_type, "поле Business type")
        self.wait_element(self.business_type_list)
        self.click(self.get_random_element(self.business_type_list), "рандомный тип")

    @allure.step("Добавление Description")
    def set_description(self, description):
        self.set_text(self.description, description, "поле Description")

    @allure.step("Добавление нового фото")
    def add_new_photo(self):
        self.click(self.add_photo_btn, "add photos")
        self.click(self.image_loader, "добавление нового фото")
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.click(self.done_photo)

    @allure.step("Добавление нового фото")
    def upload_new_photo(self):
        self.click(self.upload_a_picture, 'upload a picture')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")

    @allure.step("Добавление адреса")
    def select_address(self):
        self.click(self.add_address_btn, "add address")
        location_coordinate = self.get_element(self.address_location).center()
        self.d.click(location_coordinate[0], location_coordinate[1])
        self.click(self.address_apply_btn, "добавить выбранный адрес")

    @allure.step("Добавление телефона")
    def set_phone(self):
        phone_number = str(random.randint(10000000, 9999999999))
        self.set_text(self.phone_field, phone_number, "phone")

    @allure.step("Добавление сайта")
    def set_site(self):
        self.set_text(self.site_field, "https://test.com", "site")

    @allure.step("Переход в '{business_name}'")
    def open_business(self, business_name):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{business_name}"]',
                   business_name)

    @allure.step("Удаление '{business_name}'")
    def delete_business(self, business_name):
        self.open_business(business_name)
        self.swipe_to_element(self.delete_btn)
        self.click(self.delete_btn, "кнопка Delete")
        self.wait_title_text("Confirm action")
        self.click(self.ok_btn, "кнопка Ok")
        self.wait_hidden_element(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{business_name}"]',
                                 business_name)

    @allure.step("Редактирование '{business_name}'")
    def edit_business(self, business_name):
        self.open_business(business_name)
        new_business_name = self.set_name()
        self.set_business_type()
        self.set_description(text_250)
        self.swipe_up()
        self.swipe_up()
        self.set_phone()
        self.click_save_btn()
        self.wait_text(new_business_name)
        return new_business_name

    @allure.step("Клик по кнопке Save")
    def click_save_btn(self):
        self.click(self.save_btn, "кнопка Save")