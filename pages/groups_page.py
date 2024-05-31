from random import randint

import allure

from tests.config import *
from pages.base_page import BasePage
from common.menu import Menu
from common.permission import Permission


class GroupsPage(BasePage):
    menu = Menu()

    add_new_group_btn = 'com.yapmap.yapmap:id/action_show_option_menu'
    name_field = '//*[@resource-id="com.yapmap.yapmap:id/name_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    description_field = '//*[@resource-id="com.yapmap.yapmap:id/description_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/picture_layout"]/android.widget.FrameLayout[1]'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    create_group_btn = 'com.yapmap.yapmap:id/action_create_group'
    private_checkbox = '//*[@resource-id="com.yapmap.yapmap:id/is_private_switch"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    pin_chat_checkbox = '//*[@resource-id="com.yapmap.yapmap:id/pin_chat_switch"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    group_name_in_list = 'com.yapmap.yapmap:id/name_text_view'
    save_btn = 'com.yapmap.yapmap:id/action_save'
    back_btn = 'com.yapmap.yapmap:id/back'
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    more_options = '//*[@content-desc="More options"]'
    more_options_share = '//*[@text="Share"]'
    share_text = '//*[@resource-id="android:id/content_preview_text" and contains(@text, "Hey! Join my group")]'
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
    name_field_limit = '//*[@resource-id="com.yapmap.yapmap:id/name_field"]//*[@resource-id="com.yapmap.yapmap:id/limit_text_view" and @text="120/120"]'
    popup_yes = '//*[@text="YES"]'

    @allure.step("Добавление новой группы")
    def add_new_group(self, is_private=None, permission=True):
        group_name = 'Test group_' + str(randint(0, 999999999))
        self.click(self.add_new_group_btn, "добавить новую группу")
        self.set_text(self.name_field, group_name, "Name group")
        self.click(self.upload_a_picture, 'upload a picture')
        if permission == True:
            Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        if permission == True:
            Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "подтверждение созданного фото")
        self.set_text(self.description_field, text_250, 'поле Description')

        if is_private == 'private':
            self.swipe_up()
            self.click(self.private_checkbox, 'чекбокс Private')

        self.click(self.create_group_btn, "кнопка Создать группу")
        self.wait_element(self.group_name_in_list)
        self.swipe_down()
        self.wait_text(group_name)
        return group_name

    def click_save(self):
        self.click(self.save_btn, 'кнопка Save')

    @allure.step("Редактирование группы '{group_name}'")
    def edit_group(self, group_name):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{group_name}"]', group_name)
        self.wait_a_second()
        self.click_edit_group()
        new_group_name = 'Test group_' + str(randint(0, 999999999))
        self.set_text(self.name_field, new_group_name, "Name group")
        self.set_text(self.description_field, text_250_2, "Description")
        self.click(self.save_btn, "кнопка Save")
        self.wait_a_second()
        self.click(self.back_btn, "кнопка Назад")
        self.wait_element(self.group_name_in_list)
        self.wait_text(new_group_name)

    @allure.step("Переход на экран редактирования")
    def click_edit_group(self):
        self.click(self.d(description="User avatar image"), "аватар пользователя")

    @allure.step("Переход к экрану открытой группы '{group_name}'")
    def open_an_open_group(self, group_name):
        self.click(
            f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and not(preceding-sibling::android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/is_locked_image_view"]) and @text="{group_name}"]',
            group_name)

    @allure.step("Создание новой открытой группы и переход в нее")
    def open_or_create_open_group(self):
        self.wait_element(self.group_name_in_list)
        # count = len(self.d.xpath('//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and not(preceding-sibling::android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/is_locked_image_view"]) and contains(@text, "Test group")]').all())
        #
        # if count > 0:
        #     self.click(
        #         '//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and not(preceding-sibling::android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/is_locked_image_view"]) and contains(@text, "Test group")]',
        #         'первая группа в списке')
        #     group_name = self.get_text(self.group_card_title)
        # else:
        #     group_name = self.add_new_group()
        #     self.click(
        #         f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and not(preceding-sibling::android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/is_locked_image_view"]) and @text="{group_name}"]',
        #         group_name)
        #
        # return group_name

        group_name = self.add_new_group()
        self.click(
            f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and not(preceding-sibling::android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/is_locked_image_view"]) and @text="{group_name}"]',
            group_name)

        return group_name

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
        self.wait_element(self.share_text)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Share to Relagram")
        self.wait_text("Select chat")
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code, 'QR Code')
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Invite new member")
        self.wait_text("Invite people")
        self.press_back()
        self.wait_a_moment()

    @allure.step("Проверка кнопки Chat")
    def checking_chat_btn(self):
        self.click(self.chat_btn, "кнопка Chat")
        self.wait_element(self.message_field, "поле для текста")

    @allure.step("Проверка Invite people")
    def checking_invite_people_btn(self):
        self.click(self.invite_people_btn, "кнопка Invite people")
        self.wait_text("Invite people")

    @allure.step("Проверка Display members on map")
    def checking_members_on_map(self, group_name):
        self.click(self.members_on_map_btn, "кнопка Display members on map")
        self.wait_element(self.map_view, "карта с расположением членов группы")
        self.wait_text(group_name + " members")

    @allure.step("Проверка Blocked members")
    def checking_blocked_members(self):
        self.click(self.blocked_members_btn, "кнопка Blocked members")
        self.wait_text("Blocked users")

    @allure.step("Проверка Add admin")
    def add_admin(self):
        self.swipe_to_element(self.add_admin_btn)
        self.click(self.add_admin_btn, "кнопка Add admin")
        self.wait_text("Group administrators")

    @allure.step("Проверка Edit members")
    def edit_members(self):
        self.swipe_to_element(self.edit_members_btn)
        self.click(self.edit_members_btn, "кнопка Edit members")
        self.wait_text("Select contacts")

    @allure.step("Отправка в чат сообщения '{message}'")
    def send_message(self, message):
        self.set_text(self.message_field, message, "сообщение")
        self.click(self.send_message_btn, "кнопка отправки сообщения")
        self.wait_a_second()
        self.wait_a_second()
        self.wait_text(message)

    @allure.step("Очистка чата")
    def clear_chat_history(self):
        self.swipe_to_element(self.clear_chat_history_btn)
        self.wait_a_second()
        self.click(self.clear_chat_history_btn, "кнопка Clear chat history")
        self.wait_element(self.alert_title, "Clear chat alert")
        self.click(self.clear_chat_alert_clear_btn, "кнопка Clear")
        self.wait_element(self.message_field, "поле для текста")
        self.wait_hidden_element(self.message, "сообщения в чате")

    @allure.step("Удаление группы")
    def delete_and_leave(self, group_name):
        self.swipe_to_element(self.delete_and_leave_btn)
        self.click(self.delete_and_leave_btn, "кнопка Delete and leave")
        self.wait_element(self.alert_title, "Delete group alert")
        self.click(self.delete_group_alert_delete_btn, "кнопка Delete")
        self.d(resourceId='com.yapmap.yapmap:id/recycler_view').child(text=group_name).wait_gone(10)

    @allure.step("Вступление в группу '{group_name}'")
    def join_an_open_group(self, group_name):
        self.open_an_open_group(group_name)
        self.click_edit_group()
        self.swipe_up()

        if self.get_element(self.join_btn).count > 0:
            self.click(self.join_btn, "кнопка Join")
            self.wait_text("Congrats! your are following this group now!")
            self.click(self.join_group_congrats_ok_btn, "кнопка Ок для закрытия всплываши об успешном вступлении")

    @allure.step("Проверка кнопки Report")
    def checking_report_group_btn(self):
        self.swipe_to_element(self.report_group_btn)
        self.click(self.report_group_btn, "кнопка Report group")
        self.wait_title_text("Choose a reason")

    @allure.step("Выход из группы")
    def leave_group(self, group_name):
        self.swipe_to_element(self.leave_group_btn)
        self.click(self.leave_group_btn, "кнопка Leave")
        self.wait_alert_title("Leave group?")
        self.click(self.leave_group_confirm_btn, "кнопка Leave")
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/name_text_view" and @text="{group_name}"]', group_name)
        self.click_edit_group()
        self.swipe_up()
        self.wait_element(self.join_btn, "кнопка Join")

    @allure.step("Клик по иконке чата")
    def click_chat_icon(self):
        self.click(self.chat_btn, "иконка чата")

    @allure.step("Проверка пустого чата")
    def checking_empty_chat(self):
        self.wait_hidden_element(self.message, "сообщения в чате")

    @allure.step("Проверка лимита поля Название группы")
    def checking_group_name_limit(self, group_name):
        self.set_text(self.name_field, text_250, "Name group")
        self.wait_element(self.name_field_limit, "лимит 120/120")
        self.set_text(self.name_field, group_name, "Name group")

    @allure.step("Сохранить изменения (pop up)")
    def click_yes_popup(self):
        self.wait_text('Unsaved changes')
        self.click('//*[@text="YES"]')
        self.wait_a_second()
