import time
from random import randint

import allure

from tests.config import *
from pages.base_page import BasePage
from common.menu import Menu
from common.permission import Permission


class EventsPage(BasePage):
    menu = Menu()

    add_new_event_btn = "com.yapmap.yapmap:id/action_create"
    create_event_btn = 'com.yapmap.yapmap:id/action_show_option_menu'
    name_field = '//*[@resource-id="com.yapmap.yapmap:id/name_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    description_field = '//*[@resource-id="com.yapmap.yapmap:id/description_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/edit_event_avatar_layout"]/android.widget.FrameLayout[1]'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    create_group_btn = 'com.yapmap.yapmap:id/action_create_group'
    private_checkbox = '//*[@resource-id="com.yapmap.yapmap:id/is_private_switch"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    pin_chat_checkbox = '//*[@resource-id="com.yapmap.yapmap:id/pin_chat_switch"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    group_name_in_list = 'com.yapmap.yapmap:id/name_text_view'
    save_btn = 'com.yapmap.yapmap:id/action_save'
    back_btn = 'com.yapmap.yapmap:id/back'
    done_photo = '//*[@resource-id="com.yapmap.yapmap:id/action_done"]'
    event_name_in_list = 'com.yapmap.yapmap:id/name_text_view'
    type_select = "com.yapmap.yapmap:id/click_view"
    types = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout'

    def click_back_btn(self):
        self.click(self.d(description="Back"), "кнопка Назад")

    def add_new_event(self, is_private=None):
        event_name = 'Test event_' + str(randint(0, 999999999))
        self.click(self.add_new_event_btn, "добавить новый Event")
        self.set_text(self.name_field, event_name, "поле Channel Name")
        self.click(self.upload_a_picture, 'upload a picture')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.wait_a_second()
        self.set_text(self.description_field, text_250, 'поле Description')




        self.click(self.type_select, 'Type Selection')
        self.wait_text('Type')


        if is_private == 'private':
            self.swipe_to_element(self.private_checkbox)
            self.click(self.private_checkbox, 'чекбокс Private')

        self.click(self.create_event_btn, "кнопка Создать канал")
        self.wait_element(self.event_name_in_list)
        self.swipe_down()
        self.wait_a_second()
        self.wait_text(event_name)
        return event_name
