import random

import allure
from faker import Faker

from common.permission import Permission
from pages.base_page import BasePage
from common.menu import Menu
from common.photo import Photo
from tests.config import text_250, text_250_2

faker = Faker()


class BusinessPage(BasePage):
    menu = Menu()
    photo = Photo()

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
    # phone_field = '//*[@resource-id="com.yapmap.yapmap:id/phone_field"]/*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"]'
    # site_field = '//*[@text="Site"]'
    show_it_to_other_switch_btn = '//*[@resource-id="com.yapmap.yapmap:id/show_it_to_others_switch"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    create_new_business_btn = 'com.yapmap.yapmap:id/action_show_option_menu'
    ok_btn = 'com.yapmap.yapmap:id/ok_button'
    business_item = 'com.yapmap.yapmap:id/name_text_view'
    delete_btn = 'com.yapmap.yapmap:id/delete_button'
    save_btn = 'com.yapmap.yapmap:id/action_save'
    description_in_business_list = 'com.yapmap.yapmap:id/description_text_view'
    create_business_btn = 'com.yapmap.yapmap:id/create_business_button'
    back_btn = '//*[@content-desc="Back"]'
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    more_options = '//*[@content-desc="More options"]'
    share_text = '//*[@resource-id="android:id/content_preview_text" and contains(@text, "Hey! Join my business")]'
    qr_code = 'com.yapmap.yapmap:id/qr_code_image_view'
    message_field = 'com.yapmap.yapmap:id/input_edit_text'
    message = "com.yapmap.yapmap:id/body_text_view"
    send_message_btn = 'com.yapmap.yapmap:id/send_button_image_view'
    back_btn_2 = '//androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'

    @allure.step("Добавление новой записи Business")
    def add_new_business(self, permission=True):
        self.click_new_business_btn()

        if permission == True:
            self.photo.upload_picture()
        else:
            self.photo.upload_picture(permission=False)

        business_name = self.set_name()
        self.set_business_type()
        self.set_description("Some description")
        self.swipe_to_element(self.add_photo_btn)
        self.photo.upload_new_photo(permission=False)
        self.select_address()
        self.set_phone()
        self.swipe_up()
        self.wait_a_second()
        self.wait_a_second()
        self.set_site()
        self.click_show_it_to_other()
        self.click_create_btn()
        self.wait_a_second()
        self.click(self.ok_btn, "кнопка OK")
        self.wait_a_second()
        self.click(self.ok_btn, "кнопка OK")
        return business_name

    @allure.step("Добавление новой записи Business с максимальным заполнением полей")
    def add_new_business_with_full_fields(self):
        self.click_new_business_btn()
        # self.upload_new_photo()
        self.photo.upload_picture()
        self.set_text(self.business_name_field, text_250_2, "Business name")
        self.set_business_type()
        self.set_description(text_250)
        self.swipe_to_element(self.add_photo_btn)
        self.photo.upload_new_photo()
        # self.add_new_photo()
        self.select_address()
        self.set_phone()
        self.swipe_up()
        self.wait_a_second()
        self.wait_a_second()
        self.set_site()
        self.click_show_it_to_other()
        self.click_create_btn()
        self.click(self.ok_btn, "кнопка OK")
        self.click(self.ok_btn, "кнопка OK")

    @allure.step("Клик по кнопке Create")
    def click_create_btn(self):
        self.click(self.create_new_business_btn, "кнопка Create")
        self.wait_text("New Business profile created")

    @allure.step("Клик по переключателю Show it to other")
    def click_show_it_to_other(self):
        self.swipe_to_element(self.show_it_to_other_switch_btn)
        self.click(self.show_it_to_other_switch_btn, "Show it to other")
        self.wait_a_second()

    @allure.step("Клик по кнопке создания новой сущности")
    def click_new_business_btn(self):
        self.click(self.new_business_btn, "кнопка добавления business")
        self.wait_text("New business")

    @allure.step("Добавление названия")
    def set_name(self):
        business_name = 'Test business_' + str(random.randint(0, 999999999))
        self.set_text(self.business_name_field, business_name, "Business name")
        return business_name

    @allure.step("Добавление Business type")
    def set_business_type(self):
        self.click(self.business_type, "поле Business type")
        self.wait_element(self.business_type_list)
        self.click(self.get_random_element(self.business_type_list), "рандомный тип")

    @allure.step("Добавление Description")
    def set_description(self, description):
        self.swipe_to_element(self.description)
        self.set_text(self.description, description, "Description")

    # @allure.step("Добавление нового фото")
    # def add_new_photo(self):
    #     self.swipe_to_element(self.add_photo_btn)
    #     self.click(self.add_photo_btn, "add photos")
    #     self.click(self.image_loader, "добавление нового фото")
    #     self.wait_element(self.take_a_picture_btn)
    #     self.wait_a_second()
    #     self.click(self.take_a_picture_btn, "создание нового фото")
    #     self.click(self.take_a_picture_done_btn, "выбрать фото")
    #     self.click(self.done_photo)

    # @allure.step("Добавление нового фото")
    # def upload_new_photo(self, permission=True):
    #     self.click(self.upload_a_picture, 'upload a picture')
    #     if permission == True:
    #         Permission().close_photo_permission()
    #     self.click(self.image_loader, "добавление нового фото")
    #     if permission == True:
    #         Permission().click_while_using_the_app()
    #     self.wait_element(self.take_a_picture_btn)
    #     self.wait_a_second()
    #     self.click(self.take_a_picture_btn, "создание нового фото")
    #     self.click(self.take_a_picture_done_btn, "выбрать фото")

    @allure.step("Добавление адреса")
    def select_address(self):
        self.swipe_to_element(self.add_address_btn)
        self.click(self.add_address_btn, "add address")
        location_coordinate = self.get_element(self.address_location).center()
        self.d.click(location_coordinate[0], location_coordinate[1])
        self.click(self.address_apply_btn, "добавить выбранный адрес")

    @allure.step("Добавление телефона")
    def set_phone(self):
        self.swipe_to_element(self.phone_field)
        phone_number = str(random.randint(10000000, 9999999999))
        self.set_text(self.phone_field, phone_number, "phone")

    @allure.step("Добавление сайта")
    def set_site(self):
        self.swipe_to_element(self.site_field)
        rnd = str(random.randint(10, 99))
        self.set_text(self.site_field, f"https://test{rnd}.com", "site")

    @allure.step("Переход в '{business_name}'")
    def open_business(self, business_name):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and contains(@text, "{business_name}")]',
                   business_name)

    @allure.step("Удаление '{business_name}'")
    def delete_business(self, business_name=None):
        if business_name is not None:
            self.open_business(business_name)
            self.swipe_to_element(self.delete_btn)
            self.click(self.delete_btn, "кнопка Delete")
            self.wait_title_text("Confirm action")
            self.click(self.ok_btn, "кнопка Ok")
            self.wait_hidden_element(
                f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and contains(@text, "{business_name}")]',
                business_name)
        else:
            self.click(self.business_item, "первая запись Business")
            self.swipe_to_element(self.delete_btn)
            self.click(self.delete_btn, "кнопка Delete")
            self.wait_title_text("Confirm action")
            self.click(self.ok_btn, "кнопка Ok")

    @allure.step("Ожидание экрана Business без записей")
    def checking_empty_business_page(self):
        self.wait_element(self.create_business_btn, "кнопка Start now")

    @allure.step("Редактирование '{business_name}'")
    def edit_business(self, business_name):
        self.open_business(business_name)
        self.check_more_options()
        new_business_name = self.set_name()
        self.set_business_type()
        self.set_description(text_250)
        self.set_phone()
        self.swipe_up()
        self.wait_a_second()
        self.wait_a_second()
        self.set_site()
        self.click_save_btn()
        self.wait_text(new_business_name)
        return new_business_name

    def check_more_options(self):
        self.add_to_favorite()
        self.wait_a_second()
        self.open_more_options('Share')
        self.wait_element(self.share_text)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code)
        self.press_back()

    @allure.step("Клик по кнопке Save")
    def click_save_btn(self):
        self.click(self.save_btn, "кнопка Save")

    @allure.step("Очистка экрана Business")
    def clear_business(self):
        if self.get_elements_amount(self.business_item) > 0:
            self.delete_business()

    @allure.step("Проверка наличия записи и создание новой, если не найдено ни одной")
    def check_business_item_availability(self):
        if self.get_elements_amount(self.business_item) == 0:
            self.add_new_business()

    @allure.step("Клик по кнопке Назад")
    def click_back_btn(self):
        self.click(self.back_btn, "кнопка Назад")

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.wait_a_second()
        self.click(self.add_to_favorites_btn, "кнопка добавления в избранное")
        self.wait_a_second()

    @allure.step("Переход в доп опции группы '{option_name}'")
    def open_more_options(self, option_name):
        self.click(self.more_options, "меню группы")
        self.click(f'//*[@text="{option_name}"]', option_name)

    def user_open_business(self, business_name):
        self.swipe_to_element(f'//*[@text="{business_name}"]')
        self.click(self.d(resourceId="com.yapmap.yapmap:id/name_text_view", text=f'{business_name}'))

    def user_check_business(self):
        self.check_more_options()
        self.open_more_options('Send message')
        self.wait_text('Type message')

    @allure.step("Отправка в чат сообщения '{message}'")
    def send_message(self, message):
        self.set_text(self.message_field, message, "сообщение")
        self.click(self.send_message_btn, "кнопка отправки сообщения")
        self.wait_a_second()

    @allure.step("Проверяем чат")
    def test_chat(self):
        message = faker.text()
        self.send_message(message)
        self.wait_text(message)
        self.click(self.back_btn_2, 'кнопка <-')
        self.wait_a_second()
        self.click_back_btn()
        self.wait_a_second()
        return message


