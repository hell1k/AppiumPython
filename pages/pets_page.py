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

    # animal_type = '//*[@resource-id=com.yapmap.yapmap:id/animal_type_field]//*[@resource-id=com.yapmap.yapmap:id/click_view]'
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

    def click_back_btn(self):
        self.click(self.d(description="Back"), "кнопка Назад")

    @allure.step("Создание нового питомца")
    def add_new_pet(self):
        self.wait_text('Open for friendship')
        pet_name = 'Test pets_' + str(randint(0, 999999999))
        self.click(self.add_a_pet_btn, "добавить нового питомца")

        self.get_text(self.title_text)
        self.click(self.pop_up_ok_btn, 'кнопка ОК')

        self.add_photo()
        self.set_text(self.name_field, pet_name, "поле Name")
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
        self.set_text(self.edit_text_view, 'DOG KENNEL COLUMBUS OHIO')
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.open_for_mating_switch)
        self.click(self.open_for_mating_switch, 'Open for mating switch')

        self.swipe_to_element(self.location)
        self.click(self.location, 'Location')
        self.set_address()

        self.swipe_to_element(self.add_photos_btn)
        self.add_photo()

        self.swipe_to_element(self.post_button)
        self.get_element(self.cancel_button)
        self.click(self.post_button, 'кнопка Post')

    @allure.step("Добавить фото")
    def add_photo(self):
        self.click(self.add_photos_btn)
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.wait_a_second()
        self.click(self.done_photo)

    @allure.step("Выбор случайного типа")
    def select_random_type(self):
        self.wait_element(self.types)
        self.click(self.get_random_element(self.types), "рандомный тип")
        self.wait_a_moment()

    @allure.step("Выбрать адрес")
    def set_address(self):
        self.wait_text('Choose location')
        self.set_text(self.type_address_field, 'Novosibirsk')
        self.click(self.address_popup)
        self.click(self.map_plus_btn)
        self.wait_text('New Pet')

