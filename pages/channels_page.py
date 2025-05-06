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
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    more_options = '//*[@content-desc="More options" or @content-desc="Другие параметры"]'
    more_options_share = '//*[@text="Share"]'
    share_text = '//*[(@resource-id="android:id/content_preview_text" and contains(@text, "Hey! Join my channel")) or (@resource-id="android:id/text1" and contains(@text, "Hey! Join my channel"))]'
    more_options_share_to_yapmap = '//*[@text="Share to Relagram"]'
    more_options_qr = '//*[@text="Generate QR Code"]'
    more_options_invite = '//*[@text="Invite new member"]'
    qr_code = 'com.yapmap.yapmap:id/qr_code_image_view'
    chat_btn = 'com.yapmap.yapmap:id/open_chat_image_view'
    message_field = 'com.yapmap.yapmap:id/input_edit_text'
    send_message_btn = 'com.yapmap.yapmap:id/send_button_image_view'
    message = "com.yapmap.yapmap:id/body_text_view"
    add_members_btn = 'com.yapmap.yapmap:id/members_add_button'
    invite_people_btn = 'com.yapmap.yapmap:id/invite_people'
    members_on_map_btn = 'com.yapmap.yapmap:id/show_members_on_map_button'
    map_view = 'com.yapmap.yapmap:id/map_container_view'
    blocked_members_btn = 'com.yapmap.yapmap:id/blocked_members_button'
    blocked_comments_members_btn = 'com.yapmap.yapmap:id/show_banned_members_button'
    channel_bottom_sheet_title = 'com.yapmap.yapmap:id/title_text_view'
    add_admin_btn = 'com.yapmap.yapmap:id/edit_admins_text_view'
    edit_members_btn = 'com.yapmap.yapmap:id/edit_members_text_view'
    clear_chat_history_btn = 'com.yapmap.yapmap:id/clear_chat_history_button'
    alert_title = 'com.yapmap.yapmap:id/alertTitle'
    clear_chat_alert_clear_btn = '//*[@resource-id="android:id/button1" and @text="CLEAR"]'
    delete_channel_alert_delete_btn = '//*[@resource-id="android:id/button1" and @text="DELETE"]'
    alert_cancel_btn = '//*[@resource-id="android:id/button2" and @text="CANCEL"]'
    delete_and_leave_btn = 'com.yapmap.yapmap:id/delete_and_leave_button'
    join_btn = 'com.yapmap.yapmap:id/join_button'
    join_channel_congrats_ok_btn = '//*[@resource-id="com.yapmap.yapmap:id/ok_button"]'
    report_channel_btn = '//*[@resource-id="com.yapmap.yapmap:id/report_channel_button"]'
    leave_channel_btn = '//*[@resource-id="com.yapmap.yapmap:id/leave_button"]'
    report_reason_list = '//*[@resource-id="com.yapmap.yapmap:id/reasons_recycler_view"]//android.widget.TextView'
    leave_channel_confirm_btn = '//*[@resource-id="android:id/button1" and @text="LEAVE"]'
    leave_channel_cancel_btn = '//*[@resource-id="android:id/button1" and @text="CANCEL"]'
    done_photo = '//*[@resource-id="com.yapmap.yapmap:id/action_done"]'
    create_channel_btn = '//android.widget.Button'
    limit_channel_name = "com.yapmap.yapmap:id/limit_text_view"
    comment_button = "com.yapmap.yapmap:id/comment_button"
    x_btn_bottom_sheets = '//*[@content-desc="Close"]'

    def click_back_btn(self):
        self.click(self.d(description="Back"), "кнопка Назад")

    @allure.step("Добавление нового канала")
    def add_new_channel(self, is_private=None):
        channel_name = 'Test channel_' + str(randint(0, 999999999))
        self.click(self.add_new_channel_btn, "добавить новый канал")
        self.set_text(self.name_field, channel_name, "Channel Name")
        self.click(self.upload_a_picture, 'upload a picture')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.take_a_photo()
        self.wait_a_second()
        self.click(self.done_photo, "подтверждение созданного фото")
        self.set_text(self.description_field, text_1000, 'Description')
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
        self.set_text(self.name_field, new_channel_name, "Name group")
        self.set_text(self.description_field, text_1000_2, "Description")
        self.click(self.save_btn, "кнопка Save")
        self.click(self.d(description="Back"), "кнопка Назад")
        self.wait_element(self.channel_name_in_list)
        self.swipe_down_to_element(f'//*[@text="{channel_name}"]')
        self.wait_text(new_channel_name)

    @allure.step("Переход на экран редактирования")
    def click_edit_channel(self):
        self.wait_a_second()
        self.click(self.d(description="Channel avatar"), "аватар канала")

    @allure.step("Переход к экрану канала '{channel_name}'")
    def open_channel(self, channel_name):
        self.wait_a_second()
        self.swipe_down_to_element(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{channel_name}"]')
        self.swipe_down()
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{channel_name}"]', channel_name)
        self.wait_a_second()

    @allure.step("Переход в канал или создание нового")
    def open_or_create_channel(self):
        self.wait_element(self.channel_name_in_list)
        count = self.d(textContains='Test channel_').count

        if count > 0:
            self.click(
                '//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and not(preceding-sibling::android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/is_locked_image_view"]) and contains(@text, "Test channel")]',
                'перваый канал в списке')
            time.sleep(5)
            channel_name = self.d(textContains='Test channel_').get_text()
        else:
            channel_name = self.add_new_channel()
            self.click(
                f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and not(preceding-sibling::android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/is_locked_image_view"]) and @text="{channel_name}"]',
                channel_name)
        return channel_name

    @allure.step("Переход в приватный канал или создание нового")
    def open_or_create_private_channel(self):
        self.wait_element(self.channel_name_in_list)
        # count = self.d(textContains='Test channel_').count
        channel_name = self.add_new_channel('private')

        # if count > 0:
        #     self.click(
        #         '//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and contains(@text, "Test channel")]',
        #         'первый канал в списке')
        #     time.sleep(5)
        #     channel_name = self.d(textContains='Test channel_').get_text()
        # else:
        #     channel_name = self.add_new_channel('private')
        #     self.click(
        #         f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{channel_name}"]',
        #         channel_name)
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

    @allure.step("checking_more_options_private")
    def checking_more_options_private(self):
        self.wait_a_moment()
        self.open_more_options("Pending requests")
        self.wait_text("Pending requests")
        self.press_back()

    @allure.step("Проверка Add admin")
    def add_admin(self):
        self.swipe_to_element(self.add_admin_btn)
        self.wait_a_second()
        self.click(self.add_admin_btn, "кнопка Add admin")
        self.wait_text("Channel Administrators")

    @allure.step("Проверка Edit members")
    def edit_members(self):
        self.swipe_to_element(self.edit_members_btn)
        self.click(self.edit_members_btn, "кнопка Edit members")
        self.wait_text("Select contacts")

    @allure.step("Проверка кнопки Chat")
    def checking_chat_btn(self):
        self.click(self.chat_btn, "кнопка Chat")
        self.wait_element(self.message_field, "поле для текста")

    @allure.step("Проверка Add members")
    def checking_add_members_btn(self):
        self.swipe_to_element(self.add_members_btn)
        self.wait_a_second()
        self.click(self.add_members_btn, "кнопка Invite people")
        self.wait_text("Invite people")

    @allure.step("Проверка Display members on map")
    def checking_members_on_map(self, channel_name):
        self.click(self.members_on_map_btn, "кнопка Display members on map")
        self.wait_element(self.map_view, "карта с расположением членов группы")
        self.wait_text(channel_name + " members")

    @allure.step("Проверка Blocked members")
    def checking_blocked_members(self):
        self.wait_a_moment()
        self.click(self.blocked_members_btn, "кнопка Blocked members")
        self.wait_text("Blocked users")

    @allure.step("Отправка в чат сообщения '{message}'")
    def send_message(self, message):
        self.set_text(self.message_field, message, "сообщение")
        self.wait_a_second()
        self.click(self.send_message_btn, "кнопка отправки сообщения")
        self.wait_a_second()
        self.swipe_up()
        self.swipe_up()
        self.swipe_up()
        self.wait_text(message)
        self.wait_a_second()

    @allure.step("Очистка чата")
    def clear_chat_history(self):
        self.wait_a_second()
        self.click(self.clear_chat_history_btn, "кнопка Clear chat history")
        self.wait_element(self.alert_title, "Clear chat alert")
        self.click(self.clear_chat_alert_clear_btn, "кнопка Clear")
        self.wait_element(self.message_field, "поле для текста")
        self.wait_hidden_element(self.message, "сообщения в чате")

    @allure.step("Удаление канала")
    def delete_and_leave(self, channel_name):
        self.wait_a_second()
        self.swipe_to_element(self.delete_and_leave_btn)
        self.click(self.delete_and_leave_btn, "кнопка Delete and leave")
        self.wait_element(self.alert_title, "Delete group alert")
        self.click(self.delete_channel_alert_delete_btn, "кнопка Delete")
        self.d(resourceId='com.yapmap.yapmap:id/recycler_view').child(text=channel_name).wait_gone(10)

    @allure.step("Вступление в группу '{channel_name}'")
    def join_a_channel(self, channel_name):
        self.wait_a_second()
        self.open_channel(channel_name)
        self.join_channel()

    @allure.step("Вступление в канал")
    def join_channel(self):
        self.click_edit_channel()
        self.swipe_to_element(self.join_btn)
        self.wait_a_second()
        if self.get_element(self.join_btn).count > 0:
            self.wait_a_second()
            self.click(self.join_btn, "кнопка Join")
            self.wait_text("Congrats! your are following this channel now!")
            self.click(self.join_channel_congrats_ok_btn, "кнопка Ок для закрытия всплываши об успешном вступлении")

    @allure.step("Проверка кнопки Report")
    def checking_report_channel_btn(self):
        self.wait_a_second()
        self.click(self.report_channel_btn, "кнопка Report channel")
        self.wait_title_text("Choose a reason")

    @allure.step("Выход из группы")
    def leave_channel(self, channel_name):
        self.wait_a_second()
        self.click(self.leave_channel_btn, "кнопка Leave")
        self.wait_alert_title("Leave channel?")
        self.click(self.leave_channel_confirm_btn, "кнопка Leave")
        self.wait_a_second()
        self.swipe_down_to_element(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{channel_name}"]')
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{channel_name}"]', channel_name)
        self.click_edit_channel()
        self.swipe_to_element(self.join_btn)
        self.wait_a_second()
        self.wait_element(self.join_btn, "кнопка Join")

    @allure.step("Клик по иконке чата")
    def click_chat_icon(self):
        self.click(self.chat_btn, "иконка чата")

    @allure.step("Проверка пустого чата")
    def checking_empty_chat(self):
        self.wait_hidden_element(self.message, "сообщения в чате")

    @allure.step("Проверка лимита поля Название канала")
    def checking_channel_name_limit(self, channel_name):
        self.set_text(self.name_field, name_120, "Name channel")
        self.wait_element(self.limit_channel_name, "лимит 120/120")
        self.set_text(self.name_field, channel_name, "Name channel")

    @allure.step("Проверка комментария к сообщению в канале")
    def checking_channel_comment(self):
        self.wait_element(self.comment_button)
        self.click(self.comment_button, 'кнопка Comment')
        self.wait_element(self.channel_bottom_sheet_title)
        self.wait_text('Comments')
        comment = faker.text()
        self.send_message(comment)
        self.wait_text('Discussion')
        self.click(self.x_btn_bottom_sheets)
        self.click(self.comment_button, 'кнопка Comment')
        self.wait_text(comment)
        return comment

    @allure.step("Проверка комментария к сообщению в канале")
    def checking_channel_comment_member(self, comment):
        self.wait_a_second()
        self.click(self.comment_button, 'кнопка Comment')
        self.wait_element(self.channel_bottom_sheet_title)
        # self.wait_text('1 Comments')
        self.wait_text(comment)
        # self.wait_hidden_element(self.message_field)
        self.click(self.x_btn_bottom_sheets)
        # self.join_channel()
        self.wait_a_second()
        # self.wait_a_second()
        # self.click_back_btn()
        self.checking_channel_comment()

    @allure.step("Сохранить изменения (pop up)")
    def click_yes_popup(self):
        self.wait_text('Unsaved changes')
        self.click('//*[@text="YES"]')
        self.wait_a_second()
