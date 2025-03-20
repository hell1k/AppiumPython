import time
from random import randint

import allure
import random
from tests.config import *
from pages.base_page import BasePage
from common.menu import Menu
from common.permission import Permission


class PetsPage(BasePage):
    menu = Menu()

    add_a_pet_btn = "com.yapmap.yapmap:id/add_button"
    create_btn = "com.yapmap.yapmap:id/action_create"
    search_field = "com.yapmap.yapmap:id/search_src_text"
    pop_up_ok_btn = "com.yapmap.yapmap:id/ok_button"
    title_text = "com.yapmap.yapmap:id/title_text_view"
    name_field = "com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"
    description_field = "com.yapmap.yapmap:id/description_edit_text"
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/edit_event_avatar_layout"]/android.widget.FrameLayout[1]'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    add_photos_btn = "com.yapmap.yapmap:id/photos_field_add_photo_text_view"
    first_photo = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[2]'
    second_photo = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[3]'
    done_photo = '//*[@resource-id="com.yapmap.yapmap:id/action_done"]'
    types = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout'
    animal_type = '//*[@resource-id="com.yapmap.yapmap:id/animal_type_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    sex = '//*[@resource-id="com.yapmap.yapmap:id/sex_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    date_of_birth = '//*[@resource-id="com.yapmap.yapmap:id/date_of_birth_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    pedigree = '//*[@resource-id="com.yapmap.yapmap:id/pedigree_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    color = '//*[@resource-id="com.yapmap.yapmap:id/color_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    kennel = '//*[@resource-id="com.yapmap.yapmap:id/kennel_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    open_for_mating_switch = '//*[@resource-id="com.yapmap.yapmap:id/open_for_mating_switch"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    location = '//*[@resource-id="com.yapmap.yapmap:id/location_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
    calendar_prev = "android:id/prev"
    calendar_ok = "android:id/button1"
    cancel_button = "com.yapmap.yapmap:id/cancel_button"
    done_button = "com.yapmap.yapmap:id/done_button"
    edit_text_view = "com.yapmap.yapmap:id/edit_text_view"
    type_address_field = "com.yapmap.yapmap:id/auto_complete_text_view"
    address_popup = '//*[@text="Novosibirsk, Novosibirsk Oblast, Russia"]'
    map_plus_btn = '//*[@resource-id="com.yapmap.yapmap:id/floating_action_button"]'
    post_button = "com.yapmap.yapmap:id/post_button"
    name_in_list = 'com.yapmap.yapmap:id/name_text_view'
    share_text = '//*[@resource-id="android:id/content_preview_text" and contains(@text, "Hey! Look at the pet")]'
    qr_code = 'com.yapmap.yapmap:id/qr_code_image_view'
    more_options = 'com.yapmap.yapmap:id/action_show_option_menu'
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    send_message_btn = "com.yapmap.yapmap:id/contact_seller_text_view"
    message_field = 'com.yapmap.yapmap:id/input_edit_text'
    message = "com.yapmap.yapmap:id/body_text_view"
    send_message_chat_btn = 'com.yapmap.yapmap:id/send_button_image_view'
    back_btn_2 = '//androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'

    @allure.step("Нажатие кнопки 'Назад")
    def click_back_btn(self):
        self.click(self.d(description="Back"), "кнопка Назад")

    @allure.step("Создание нового питомца")
    def add_new_pet_btn(self):
        self.click(self.create_btn, "добавить нового питомца")

    @allure.step("Создание нового питомца")
    def add_new_pet(self):
        pet_name = 'Test pets_' + str(randint(0, 999999999))
        self.set_text(self.name_field, pet_name, "поле Name")
        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_250, 'поле Description')
        self.swipe_to_element(self.animal_type)
        self.click(self.animal_type, 'Animal type')
        self.wait_text('Animal type')
        self.select_random_type()
        self.swipe_to_element(self.sex)
        self.click(self.sex, 'Sex')
        self.wait_text('Sex')
        self.select_random_type()
        self.swipe_to_element(self.date_of_birth)
        self.click(self.date_of_birth, 'Date of Birth')
        self.click(self.calendar_prev, 'кнопка назад на календаре')
        self.click(self.calendar_prev, 'кнопка назад на календаре')
        random_date = random.randrange(1, 28)
        self.click(f'//*[@text={str(random_date)}]', f'дата {random_date}')
        self.click(self.calendar_ok, 'кнопка OK на календаре')
        self.swipe_to_element(self.pedigree)
        self.click(self.pedigree, 'Pedigree')
        self.wait_text('Pedigree')
        self.select_random_type()
        self.swipe_to_element(self.color)
        self.click(self.color, 'Color')
        self.wait_text('Color')
        self.select_random_type()
        self.swipe_to_element(self.kennel)
        self.click(self.kennel, 'Kennel')
        assert self.get_text(self.title_text) == 'Kennel'
        self.get_element(self.cancel_button)
        self.get_element(self.done_button)
        kennel_name = 'DOG KENNEL COLUMBUS OHIO'
        self.set_text(self.edit_text_view, kennel_name)
        self.click(self.done_button, 'кнопка Done')
        self.swipe_to_element(self.open_for_mating_switch)
        self.click(self.open_for_mating_switch, 'Open for mating switch')
        self.swipe_to_element(self.location)
        self.click(self.location, 'Location')
        self.set_address()
        self.swipe_to_element(self.add_photos_btn)
        self.add_photo_without_permissions()
        self.swipe_to_element(self.post_button)
        self.get_element(self.cancel_button)
        self.click(self.post_button, 'кнопка Post')
        # self.wait_text('You pet has been accepted')
        # self.get_screen()
        # self.wait_text('Others can see it in a few minutes. We wish you a successful sale.')
        return pet_name

    @allure.step("check_pet_in_list")
    def check_pet_in_list(self, pet_name):
        self.wait_element(self.name_in_list)
        self.swipe_down()
        self.wait_text(pet_name)

    @allure.step("Добавить фото")
    def add_photo(self):
        self.click(self.add_photos_btn, 'кнопка Add photos')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.wait_a_second()
        self.click(self.done_photo, 'кнопка Done')

    @allure.step("Добавить фото")
    def add_photo_without_permissions(self):
        self.click(self.add_photos_btn, 'кнопка Add photos')
        self.click(self.image_loader, "добавление нового фото")
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.wait_a_second()
        self.wait_a_second()
        self.click(self.done_photo, 'кнопка Done')

    @allure.step("Выбор случайного типа")
    def select_random_type(self):
        self.wait_element(self.types)
        element = self.get_random_element(self.types)
        self.click(element, f"{element.text}")
        self.wait_a_second()

    @allure.step("Выбрать адрес")
    def set_address(self, city_name='Novosibirsk'):
        self.wait_text('Choose location')
        self.set_text(self.type_address_field, city_name)
        self.click(self.address_popup, 'адрес из всплывашки')
        self.click(self.map_plus_btn, 'кнопка + на карте')
        self.wait_text('New Pet')

    @allure.step("Открытие карточки питомца")
    def open_pet(self, pet_name):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{pet_name}"]', pet_name)

    @allure.step("Редактирование питомца")
    def edit_pet(self):
        self.click(self.more_options, 'кнопка ... в верхнем правом углу')
        self.click('//*[@text="Edit"]')
        self.add_photo_without_permissions()
        new_pet_name = 'Test pets_' + str(randint(0, 999999999))
        self.set_text(self.name_field, new_pet_name, "поле Name")
        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_250_2, "поле Description")
        self.swipe_to_element(self.animal_type)
        self.click(self.animal_type, 'Animal type')
        self.wait_text('Animal type')
        self.select_random_type()
        self.wait_a_second()
        self.swipe_to_element(self.sex)
        self.click(self.sex, 'Sex')
        self.wait_text('Sex')
        self.select_random_type()

        self.swipe_to_element(self.date_of_birth)
        self.click(self.date_of_birth, 'Date of Birth')
        self.click(self.calendar_prev, 'кнопка назад на календаре')
        self.click(self.calendar_prev, 'кнопка назад на календаре')
        random_date = random.randrange(1, 28)
        self.click(f'//*[@text={str(random_date)}]', f'дата {random_date}')
        self.click(self.calendar_ok, 'кнопка OK на календаре')

        self.swipe_to_element(self.pedigree)
        self.click(self.pedigree, 'Pedigree')
        self.wait_text('Pedigree')
        self.select_random_type()

        self.swipe_to_element(self.color)
        self.click(self.color, 'Color')
        self.wait_text('Color')
        self.select_random_type()

        self.swipe_to_element(self.kennel)
        self.click(self.kennel, 'Kennel')
        assert self.get_text(self.title_text) == 'Kennel'
        self.get_element(self.cancel_button)
        self.get_element(self.done_button)
        kennel_name = 'CATS KENNEL COLUMBUS OHIO'
        self.set_text(self.edit_text_view, kennel_name)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.open_for_mating_switch)
        self.click(self.open_for_mating_switch, 'Open for mating switch')

        self.swipe_to_element(self.add_photos_btn)
        self.add_photo_without_permissions()

        self.swipe_to_element(self.post_button)
        self.get_element(self.cancel_button)
        self.click(self.post_button, 'кнопка Post')
        self.wait_text(new_pet_name)
        self.click_back_btn()
        self.wait_element(self.name_in_list)
        self.swipe_down()
        self.wait_text(new_pet_name)
        self.wait_text(kennel_name)

        return new_pet_name

    @allure.step("Удаление питомца")
    def delete_pet(self, pet_name):
        self.click(self.more_options, 'кнопка ... в верхнем правом углу')
        self.click('//*[@text="Delete"]')
        self.click(self.pop_up_ok_btn, 'кнопка ОК на popup')
        self.swipe_down()
        self.wait_a_second()
        self.d(resourceId='com.yapmap.yapmap:id/recycler_view').child(text=pet_name).wait_gone(10)

    @allure.step("Переход в доп опции '{option_name}'")
    def open_more_options(self, option_name):
        self.click(self.more_options, "меню группы")
        self.click(f'//*[@text="{option_name}"]', option_name)

    @allure.step("Проверка меню ... в шапке")
    def checking_more_options(self):
        self.wait_a_moment()
        self.open_more_options("Edit")
        self.wait_text('Editing')
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Share")
        self.wait_element(self.share_text)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Delete")
        self.wait_text('Delete pet')
        self.wait_text('Are you sure want to delete the pet? This action cannot be undone')
        self.wait_element(self.cancel_button)
        self.wait_element(self.pop_up_ok_btn)
        self.click(self.cancel_button)
        self.wait_a_moment()
        self.open_more_options("Cancel")
        self.wait_hidden_element(self.cancel_button)

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.click(self.add_to_favorites_btn, "кнопка добавления в избранное")

    @allure.step("Проверка меню ... в шапке")
    def checking_more_options_user(self):
        self.wait_a_moment()
        self.open_more_options("Share")
        self.wait_element(self.share_text)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Message")
        self.wait_text('Pets')
        self.wait_text('On behalf of which pet there will be communication?')
        self.press_back()
        self.open_more_options("Complain")
        self.wait_text('Choose a reason')
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Cancel")
        self.wait_hidden_element(self.cancel_button)

    @allure.step("Перейти в чат")
    def click_send_message(self):
        self.swipe_to_element(self.send_message_btn)
        self.click(self.send_message_btn, 'нажать кнопку Send message')
        self.wait_text('Pets')
        self.wait_text('On behalf of which pet there will be communication?')

    @allure.step("Проверка сообщения You don't have any Pets here yet")
    def user_dont_have_pets_msg_check(self):
        if self.get_elements_amount(self.cancel_button) > 0:
        # self.wait_text("You don't have any Pets here yet")
        # self.wait_text(
        #     "You can't use the Pets feature because you don't have any Pets added to your profile yet. Do you wish to create?")
            self.click_cancel()

    @allure.step("Нажатие кнопки 'Отменить")
    def click_cancel(self):
        self.click(self.cancel_button, 'кнопка Cancel')

    @allure.step("Нажатие кнопки 'Ок")
    def click_ok(self):
        self.click(self.pop_up_ok_btn, 'кнопка OK')

    @allure.step("Проверка сообщения Pets is a public platform and can ...")
    def pets_check_msg(self):
        self.wait_text(
            'Pets is a public platform and can be seen by anyone on Relagram. See our Terms and Condition to avoid listing violations. Violators will be banned from using Relagram forever')

    @allure.step("Проверка пустого чата")
    def checking_empty_chat(self):
        self.wait_hidden_element(self.message, "сообщения в чате")

    @allure.step("Отправка в чат сообщения '{message}'")
    def send_message(self, message):
        self.set_text(self.message_field, message, "сообщение")
        self.click(self.send_message_chat_btn, "кнопка отправки сообщения")
        self.wait_a_second()
        self.wait_a_second()
        self.wait_text(message)

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

    @allure.step("Поиск питомца по имени")
    def search_pet_name(self, pet_name):
        self.set_text(self.search_field, pet_name)

    @allure.step("wait_pets_page")
    def wait_pets_page(self):
        self.wait_a_second()
        self.wait_text('Pets')

