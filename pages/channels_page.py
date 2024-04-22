import time
from random import randint

import allure

from tests.config import *
from pages.base_page import BasePage
from common.menu import Menu
from common.permission import Permission


class ChannelsPage(BasePage):
    menu = Menu()

    title = 'com.yapmap.yapmap:id/toolbar'
    add_new_channel_btn = "com.yapmap.yapmap:id/action_show_option_menu"
    search_field = "com.yapmap.yapmap:id/search_src_text"
    create_btn = "com.yapmap.yapmap:id/action_create"
    upload_a_picture = "com.yapmap.yapmap:id/photos_field_add_photo_text_view"
    name_field = "com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"
    channel_description = "com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"
    private_switch = '//*[@resource-id="com.yapmap.yapmap:id/is_private_switch"]'
    notification_switch = '//*[@resource-id="com.yapmap.yapmap:id/notifications_on_switch"]'

    add_new_group_btn = 'com.yapmap.yapmap:id/action_show_option_menu'
    description_field = '//*[@resource-id="com.yapmap.yapmap:id/description_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    create_group_btn = 'com.yapmap.yapmap:id/action_create_group'
    private_checkbox = '//*[@resource-id="com.yapmap.yapmap:id/is_private_switch"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    pin_chat_checkbox = '//*[@resource-id="com.yapmap.yapmap:id/pin_chat_switch"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    channel_name_in_list = 'com.yapmap.yapmap:id/name_text_view'
    save_btn = 'com.yapmap.yapmap:id/action_save'
    back_btn = 'com.yapmap.yapmap:id/back'
    # back_btn = 'com.yapmap.yapmap:id/back'
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    more_options = '//*[@content-desc="More options"]'
    more_options_share = '//*[@text="Share"]'
    share_text = '//*[@resource-id="android:id/content_preview_text" and contains(@text, "Hey! Join my channel")]'
    more_options_share_to_yapmap = '//*[@text="Share to YapMap"]'
    more_options_qr = '//*[@text="Generate QR Code"]'
    more_options_invite = '//*[@text="Invite new member"]'
    qr_code = 'com.yapmap.yapmap:id/qr_code_image_view'
    chat_btn = 'com.yapmap.yapmap:id/open_chat_image_view'
    message_field = 'com.yapmap.yapmap:id/input_edit_text'
    send_message_btn = 'com.yapmap.yapmap:id/send_button_image_view'
    message = "com.yapmap.yapmap:id/body_text_view"
    invite_people_btn = 'com.yapmap.yapmap:id/invite_people'
    members_on_map_btn = 'com.yapmap.yapmap:id/show_members_on_map_button'
    map_view = 'com.yapmap.yapmap:id/map_container_view'
    blocked_members_btn = 'com.yapmap.yapmap:id/show_blocked_members_button'
    blocked_comments_members_btn = 'com.yapmap.yapmap:id/show_banned_members_button'
    group_card_title = 'com.yapmap.yapmap:id/title_text_view'
    add_admin_btn = 'com.yapmap.yapmap:id/edit_admins_text_view'
    edit_members_btn = 'com.yapmap.yapmap:id/edit_members_text_view'
    clear_chat_history_btn = 'com.yapmap.yapmap:id/clear_chat_history_button'
    alert_title = 'com.yapmap.yapmap:id/alertTitle'
    clear_chat_alert_clear_btn = '//*[@resource-id="android:id/button1" and @text="CLEAR"]'
    delete_group_alert_delete_btn = '//*[@resource-id="android:id/button1" and @text="DELETE"]'
    alert_cancel_btn = '//*[@resource-id="android:id/button2" and @text="CANCEL"]'
    delete_and_leave_btn = 'com.yapmap.yapmap:id/delete_and_leave_button'
    join_btn = 'com.yapmap.yapmap:id/join_button'
    join_group_congrats_ok_btn = '//*[@resource-id="com.yapmap.yapmap:id/ok_button"]'
    report_group_btn = '//*[@resource-id="com.yapmap.yapmap:id/report_group_button"]'
    leave_group_btn = '//*[@resource-id="com.yapmap.yapmap:id/leave_button"]'
    report_reason_list = '//*[@resource-id="com.yapmap.yapmap:id/reasons_recycler_view"]//android.widget.TextView'
    leave_group_confirm_btn = '//*[@resource-id="android:id/button1" and @text="LEAVE"]'
    leave_group_cancel_btn = '//*[@resource-id="android:id/button1" and @text="CANCEL"]'
    done_photo = '//*[@resource-id="com.yapmap.yapmap:id/action_done"]'
    create_channel_btn = '//android.widget.Button'

    @allure.step("Добавление нового канала")
    def add_new_channel(self, is_private=None):
        channel_name = 'Test channel_' + str(randint(0, 999999999))
        self.click(self.add_new_channel_btn, "добавить новый канал")
        self.set_text(self.name_field, channel_name, "поле Channel Name")
        self.click(self.upload_a_picture, 'upload a picture')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.click(self.done_photo, "подтверждение созданного фото")
        self.set_text(self.description_field, text_1000, 'поле Description')
        if is_private == 'private':
            self.swipe_up()
            self.click(self.private_checkbox, 'чекбокс Private')

        self.click(self.create_channel_btn, "кнопка Создать канал")
        self.wait_element(self.channel_name_in_list)
        self.swipe_down()
        self.wait_a_second()
        self.wait_text(channel_name)
        return channel_name

    @allure.step("Редактирование канала '{channel_name}'")
    def edit_channel(self, channel_name):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{channel_name}"]', channel_name)
        self.click_edit_channel()
        new_channel_name = 'Test channel_' + str(randint(0, 999999999))
        self.set_text(self.name_field, new_channel_name, "поле Name group")
        self.set_text(self.description_field, text_1000_2, "поле Description")
        self.click(self.save_btn, "кнопка Save")
        # self.click(self.back_btn, "кнопка Назад")
        self.click(self.d(description="Back"), "кнопка Назад")
        self.wait_element(self.channel_name_in_list)
        self.wait_text(new_channel_name)

    @allure.step("Переход на экран редактирования")
    def click_edit_channel(self):
        self.wait_a_second()
        self.click(self.d(description="Channel avatar"), "аватар канала")

    @allure.step("Переход к экрану группы '{group_name}'")
    def open_channel(self, channel_name):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{channel_name}"]', channel_name)

    @allure.step("Переход в канал или создание нового")
    def open_or_create_channel(self):
        self.wait_element(self.channel_name_in_list)
        count = self.d(textContains='Test channel_').count

        if count > 0:
            self.click('//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and contains(@text, "Test channel")]',
                       'первая группа в списке')
            time.sleep(5)
            channel_name = self.d(textContains='Test channel_').get_text()
        else:
            channel_name = self.add_new_channel()
            self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{channel_name}"]', channel_name)
        return channel_name

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.click(self.add_to_favorites_btn, "кнопка добавления в избранное")

    @allure.step("Переход в доп опции группы '{option_name}'")
    def open_more_options(self, option_name):
        self.click(self.more_options, "меню группы")
        self.click(f'//*[@text="{option_name}"]', option_name)

    @allure.step("Проверка меню ... в шапке")
    def checking_more_options(self):
        self.open_more_options("Share")
        self.wait_element(self.share_text, "текст приглашения в группу")
        self.press_back()
        self.open_more_options("Share to YapMap")
        self.wait_text("Select chat")
        self.press_back()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code, 'QR Code')
        self.press_back()
        self.open_more_options("Invite new member")
        self.wait_text("Invite people")
        self.press_back()

    @allure.step("Проверка Add admin")
    def add_admin(self):
        self.click(self.add_admin_btn, "кнопка Add admin")
        self.wait_text("Channel Administrators")

    @allure.step("Проверка Edit members")
    def edit_members(self):
        self.click(self.edit_members_btn, "кнопка Edit members")
        self.wait_text("Select contacts")
