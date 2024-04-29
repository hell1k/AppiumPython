import time
from random import randint

import allure
import random
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
    private_checkbox = '//*[@text="Private"]/..'
    private_text = '//*[@text="Private"]'
    pin_chat_checkbox = '//*[@text="Pin chat"]/..'
    group_name_in_list = 'com.yapmap.yapmap:id/name_text_view'
    save_btn = 'com.yapmap.yapmap:id/action_save'
    back_btn = 'com.yapmap.yapmap:id/back'
    done_photo = '//*[@resource-id="com.yapmap.yapmap:id/action_done"]'
    event_name_in_list = 'com.yapmap.yapmap:id/name_text_view'
    type_selection = "com.yapmap.yapmap:id/click_view"
    types = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout'
    add_photos_btn = "com.yapmap.yapmap:id/photos_field_add_photo_text_view"
    first_photo = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[2]'
    second_photo = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[3]'
    date_start = "com.yapmap.yapmap:id/start_date_edit_text"
    date_end = "com.yapmap.yapmap:id/end_date_edit_text"
    time_start = "com.yapmap.yapmap:id/start_time_edit_text"
    time_end = "com.yapmap.yapmap:id/end_time_edit_text"
    live_event_check_box = "com.yapmap.yapmap:id/live_event_check_box"
    online_event_check_box = "com.yapmap.yapmap:id/online_event_check_box"
    address_select_btn = '//*[@text="Address"]/..'
    type_address_field = "com.yapmap.yapmap:id/auto_complete_text_view"
    address_popup = '//*[@text="Novosibirsk, Novosibirsk Oblast, Russia"]'
    map_plus_btn = '//*[@resource-id="com.yapmap.yapmap:id/floating_action_button"]'
    number_of_members_field = '//*[@text="Number of members (optional)"]'
    calendar_next_btn = '//*[@resource-id="android:id/next"]'
    calendar_ok = '//*[@resource-id="android:id/button1"]'
    notification_checkbox = '//*[@text="Notifications"]/..'
    show_it_to_others_checkbox = '//*[@text="Show it to others"]/..'
    show_me_to_this_community = '//*[@text="Show me to this community"]/..'
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    more_options = '//*[@content-desc="More options"]'
    more_options_share = '//*[@text="Share"]'
    share_text = '//*[@resource-id="android:id/content_preview_text" and contains(@text, "Hey! Join to my event")]'
    more_options_share_to_relagram = '//*[@text="Share to Relagram"]'
    more_options_qr = '//*[@text="Generate QR Code"]'
    more_options_invite = '//*[@text="Invite new member"]'
    qr_code = 'com.yapmap.yapmap:id/qr_code_image_view'
    limit_name = "com.yapmap.yapmap:id/limit_text_view"
    alert_title = 'com.yapmap.yapmap:id/alertTitle'
    delete_channel_alert_delete_btn = '//*[@resource-id="android:id/button1" and @text="DELETE"]'
    alert_cancel_btn = '//*[@resource-id="android:id/button2" and @text="CANCEL"]'
    delete_and_leave_btn = 'com.yapmap.yapmap:id/delete_and_leave_button'
    edit_members_btn = 'com.yapmap.yapmap:id/edit_members_text_view'

    def click_back_btn(self):
        self.click(self.d(description="Back"), "кнопка Назад")

    @allure.step("Выбор случайного типа")
    def select_random_type(self):
        self.click(self.type_selection)
        self.wait_element(self.types)
        self.click(self.get_random_element(self.types), "рандомный тип")
        self.wait_a_moment()

    @allure.step("Создание нового эвента")
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

        self.select_random_type()

        self.swipe_to_element(self.add_photos_btn)
        self.click(self.add_photos_btn)
        self.click(self.first_photo)
        # self.click(self.second_photo)
        self.click(self.done_photo)

        self.click(self.date_start)
        self.click(self.calendar_next_btn)
        random_date = random.randrange(1, 28)
        self.click(f'//*[@text={str(random_date)}]', f'дата {random_date}')
        self.click(self.calendar_ok, "кнопка Ок")

        self.swipe_to_element(self.date_end)
        self.click(self.date_end)
        self.click(self.calendar_next_btn)
        random_date = random.randrange(1, 28)
        self.click(f'//*[@text={str(random_date)}]', f'дата {random_date}')
        self.click(self.calendar_ok, "кнопка Ок")

        self.click(self.online_event_check_box)


        self.swipe_to_element(self.address_select_btn)
        self.click(self.address_select_btn)
        self.wait_text('Choose location')
        self.set_text(self.type_address_field, 'Novosibirsk')
        self.click(self.address_popup)
        self.click(self.map_plus_btn)
        self.wait_text('New event')

        self.swipe_to_element(self.number_of_members_field)
        random_number = str(random.randrange(5, 1000))
        self.click(self.number_of_members_field)
        self.wait_a_moment()
        self.set_text(self.number_of_members_field, random_number)

        if is_private == 'private':
            self.swipe_to_element(self.private_text)
            self.click(self.private_checkbox, 'чекбокс Private')

        self.swipe_to_element(self.show_me_to_this_community)
        self.click(self.notification_checkbox, 'чекбокс Notification')
        self.click(self.show_it_to_others_checkbox, 'чекбокс Show it to others')
        self.click(self.show_me_to_this_community, 'чекбокс Show me to this community')

        self.click(self.create_event_btn, "кнопка Создать")
        self.wait_element(self.event_name_in_list)
        self.swipe_down()
        self.wait_a_second()
        self.wait_text(event_name)
        return event_name

    @allure.step("Редактирование эвента '{event_name}'")
    def edit_event(self, event_name):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{event_name}"]', event_name)
        new_event_name = 'Test event_' + str(randint(0, 999999999))
        self.set_text(self.name_field, new_event_name, "поле Name event")
        self.set_text(self.description_field, text_250_2, "поле Description")
        self.swipe_to_element(self.type_selection)
        self.select_random_type()
        self.swipe_to_element(self.live_event_check_box)
        self.click(self.live_event_check_box)
        self.click(self.save_btn, "кнопка Save")
        self.wait_element(self.event_name_in_list)
        self.wait_text(new_event_name)

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.click(self.add_to_favorites_btn, "кнопка добавления в избранное")

    @allure.step("Переход в доп опции группы '{option_name}'")
    def open_more_options(self, option_name):
        self.click(self.more_options, "меню группы")
        self.click(f'//*[@text="{option_name}"]', option_name)

    @allure.step("Проверка меню ... в шапке")
    def checking_more_options(self):
        self.wait_a_moment()
        self.open_more_options("Share")
        self.wait_element(self.share_text)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Share to Relagram")
        self.wait_text("Select chat")
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Invite new member")
        self.wait_text("Invite people")
        self.press_back()

    def checking_more_options_private(self):
        self.wait_a_moment()
        self.open_more_options("Pending requests")
        self.wait_text("Pending requests")
        self.press_back()

    @allure.step("Переход к экрану оюытия '{event_name}'")
    def open_event(self, event_name):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{event_name}"]', event_name)

    @allure.step("Проверка лимита поля Название канала")
    def checking_event_name_limit(self, event_name):
        self.set_text(self.name_field, name_120, "Name event")
        self.wait_element(self.limit_name, "лимит 120/120")
        self.set_text(self.name_field, event_name, "Name event")

    @allure.step("Проверка Edit members")
    def edit_members(self):
        self.swipe_to_element(self.edit_members_btn)
        self.click(self.edit_members_btn, "кнопка Edit members")
        self.wait_text("Select contacts")

    @allure.step("Удаление события")
    def delete_and_leave(self, event_name):
        self.wait_a_second()
        self.click(self.delete_and_leave_btn, "кнопка Delete and leave")
        self.wait_element(self.alert_title, "Delete group alert")
        self.click(self.delete_channel_alert_delete_btn, "кнопка Delete")
        self.d(resourceId='com.yapmap.yapmap:id/recycler_view').child(text=event_name).wait_gone(10)