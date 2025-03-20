import time
from random import randint

import allure
import random
from tests.config import *
from pages.base_page import BasePage
from common.menu import Menu
from common.permission import Permission


class ChatsPage(BasePage):
    menu = Menu()
    permission = Permission()

    people_tab = '//*[@text="People"]'
    pets_tab = '//*[@text="Pets"]'
    market_tab = '//*[@text="Market"]'
    business_tab = '//*[@text="Businesses"]'
    jobs_tab = '//*[@text="Jobs"]'
    tab_layout = '//*[@resource-id="com.yapmap.yapmap:id/tab_layout"]'
    i_own = '//*[@resource-id="com.yapmap.yapmap:id/owner_layout"]'
    i_am_interested = '//*[@resource-id="com.yapmap.yapmap:id/member_layout"]'
    business_chats = '//*[@resource-id="com.yapmap.yapmap:id/business_chats_recycler_view"]/android.widget.LinearLayout'
    emoji_btn = "com.yapmap.yapmap:id/emoji_layout_button_image_view"
    stickers_btn = "com.yapmap.yapmap:id/stickers_layout_button_image_view"
    images_btn = "com.yapmap.yapmap:id/images_layout_button_image_view"
    camera_btn = "com.yapmap.yapmap:id/camera_layout_button_image_view"
    attachment_btn = "com.yapmap.yapmap:id/attachment_layout_button_image_view"
    emoji_list = '//*[@resource-id="com.yapmap.yapmap:id/emoji_container_layout"]/android.widget.LinearLayout[1]/android.widget.ImageView'
    send_button = "com.yapmap.yapmap:id/send_button_image_view"
    like_btn = "com.yapmap.yapmap:id/primary_emoji_image_view"
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    message_edit_text = "com.yapmap.yapmap:id/message_edit_text"
    search_plate = "com.yapmap.yapmap:id/search_src_text"
    add_for_free_button = "com.yapmap.yapmap:id/add_for_free_button"
    add_button = "com.yapmap.yapmap:id/add_button"
    back_button = "com.yapmap.yapmap:id/back_button"
    cancel_button = "com.yapmap.yapmap:id/cancel_button"
    my_notes = '//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout[1]'
    menu_tabs = "com.yapmap.yapmap:id/tab_layout"
    back_btn_2 = '//androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'
    back_btn = '//*[@content-desc="Back"]'
    message_field = 'com.yapmap.yapmap:id/input_edit_text'
    message = "com.yapmap.yapmap:id/body_text_view"
    send_message_btn = 'com.yapmap.yapmap:id/send_button_image_view'
    sticker_pack_name = "com.yapmap.yapmap:id/sticker_pack_name_text_view"
    delete_btn = "com.yapmap.yapmap:id/delete_button"
    ok_btn = "com.yapmap.yapmap:id/ok_button"
    comment_button = "com.yapmap.yapmap:id/comment_button"
    x_btn_bottom_sheets = '//*[@content-desc="Close"]'
    bottom_sheet_title = 'com.yapmap.yapmap:id/title_text_view'
    done_btn = "com.yapmap.yapmap:id/action_done"
    find_button = "com.yapmap.yapmap:id/find_button"
    create_event_button = "com.yapmap.yapmap:id/create_event_button"
    create_group_button = "com.yapmap.yapmap:id/create_group_button"

    @allure.step("Клик по кнопке Назад")
    def click_back_btn(self):
        self.click(self.back_btn, "кнопка Назад")

    # def click_people_tab(self):
    #     self.click(self.people_tab, 'вкладка People')
    #
    # def click_pets_tab(self):
    #     self.swipe_to_element_in_tab(self.pets_tab)
    #     self.click(self.pets_tab, 'вкладка Pets')
    #
    # def click_market_tab(self):
    #     self.swipe_to_element_in_tab(self.market_tab)
    #     self.click(self.market_tab, 'вкладка Market')
    #
    # def click_business_tab(self):
    #     self.wait_a_second()
    #     self.wait_a_second()
    #     self.swipe_to_element_in_tab(self.business_tab)
    #     self.click(self.business_tab, 'вкладка Business')
    #
    # def click_jobs_tab(self):
    #     self.swipe_to_element_in_tab(self.jobs_tab)
    #     self.click(self.jobs_tab, 'вкладка Jobs')

    @allure.step("Проверяем чат раздела Pets")
    def check_pets_message(self, pet_name, user_pet_name, message):
        self.open_pets_tab()
        self.click(self.i_own)
        self.click(f'//*[@text="{pet_name}"]', pet_name)
        self.wait_a_second()
        self.click(f'//*[@text="{user_pet_name}"]', user_pet_name)
        self.wait_a_second()
        self.wait_text(message)

    @allure.step("Проверяем чат раздела Events")
    def check_events_message(self, event_name, message):
        self.open_events_tab()
        self.click(f'//*[@text="{event_name}"]')
        self.wait_a_second()
        self.wait_text(message)

    @allure.step("click_i_own")
    def click_i_own(self):
        self.click(self.i_own, 'I Own')

    @allure.step("click_i_am_interested")
    def click_i_am_interested(self):
        self.click(self.i_am_interested, 'I am interested')

    @allure.step("Проверяем чат раздела Business")
    def check_business_message(self, business_name, new_message):
        self.open_businesses_tab()
        self.click(self.i_own)
        self.click(self.business_chats)
        self.wait_text(business_name)
        self.wait_a_second()
        self.wait_text(new_message)

    @allure.step("Проверяем чат раздела Job")
    def check_job_message(self, position_name, message):
        self.open_jobs_tab()
        self.click(self.i_own)
        self.click(f'//*[@text="{position_name}"]', position_name)
        self.wait_a_second()
        self.wait_text(message)

    @allure.step("Проверяем чат раздела Market")
    def check_market_message(self, message):
        self.open_market_tab()
        self.click(self.i_own)
        self.wait_text(message)
        self.click(f'//*[@text="{message}"]')
        self.wait_text(message)

    @allure.step("Отправить emoji в чат")
    def check_send_emoji(self):
        # self.click(self.emoji_btn, 'кнопка Emoji')
        # self.click(self.get_random_element(self.emoji_list), 'рандомный emoji')
        # self.click(self.send_button)
        print('Раскомментить после правки бага')

    @allure.step("Отправить sticker в чат")
    def check_send_sticker(self):
        self.click(self.stickers_btn, 'кнопка Sticker')
            # if self.get_elements_amount(self.sticker_pack_name) == 0:
        if self.get_elements_amount('//*[@content-desc="Cosmic Tiger"]') == 0:
            self.add_sticker_pack()
        self.click(self.stickers_btn, 'кнопка Sticker')
        self.click('//*[@resource-id="com.yapmap.yapmap:id/icons_recycler_view"]/android.widget.LinearLayout[3]')
        self.click(self.get_random_element(
            '//*[@resource-id="com.yapmap.yapmap:id/stickers_flexbox_layout"]/android.widget.FrameLayout'))

    @allure.step("Удаление стикер пака")
    def del_sticker_pack(self):
        self.click(self.stickers_btn, 'кнопка Sticker')
        self.click('//*[@resource-id="com.yapmap.yapmap:id/icons_recycler_view"]/android.widget.LinearLayout[3]')
        self.click(self.delete_btn, 'кнопка x')
        self.click(self.ok_btn, 'кнопка OK')
        self.wait_hidden_element(self.sticker_pack_name)

    @allure.step("Добавление стикер пака")
    def add_sticker_pack(self):
        self.click('//*[@resource-id="com.yapmap.yapmap:id/icons_recycler_view"]/android.widget.LinearLayout[1]')
        self.wait_text('Enter at least 3 characters')
        self.set_text(self.search_plate, 'tiger')
        self.wait_a_second()
        self.click(self.add_for_free_button, 'кнопка Add free')
        self.wait_text('Sticker pack')
        self.click(self.add_button, 'кнопка ADD FREE')
        self.wait_text('ADDED')
        self.click(self.back_button, 'кнопка назад')
        self.click(self.cancel_button, 'кнопка Cancel')

    @allure.step("Добавление комментария у стикер паку")
    def add_sticker_pack_comment(self):
        self.click('com.yapmap.yapmap:id/stickers_layout_button_image_view')
        self.click('com.yapmap.yapmap:id/sticker_picture_view')
        self.wait_text('Enter at least 3 characters')
        self.set_text(self.search_plate, 'tiger')
        self.wait_a_second()
        self.click(self.add_for_free_button, 'кнопка Add free')
        self.wait_text('Sticker pack')
        self.click(self.add_button, 'кнопка ADD FREE')
        self.wait_text('ADDED')
        self.click(self.back_button, 'кнопка назад')
        self.click(self.cancel_button, 'кнопка Cancel')

        # self.click(
        #     self.d('//*[@resource-id="com.yapmap.yapmap:id/icons_recycler_view"]/android.widget.LinearLayout[2]'))
        # self.wait_text('Upload your stickers now!')

    @allure.step("Отправить images в чат")
    def check_send_images(self):
        self.click(self.images_btn)
        # self.click(self.d(resourceId="com.google.android.documentsui:id/sub_menu"))
        self.click(self.get_random_element('//android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/picture_view"]'))
        self.wait_a_moment()
        self.click(self.done_btn)
        self.set_text(self.message_edit_text, 'Random text')
        self.click(self.send_button)

    @allure.step("Отправить images в чат")
    def check_send_images_type_2(self):
        self.click(self.images_btn)
        self.click(self.get_random_element('//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup'))
        self.click(self.done_btn)

    @allure.step("Отправить images с камеры в чат")
    def check_send_images_from_camera(self):
        self.click(self.camera_btn)
        self.permission.click_while_using_the_app()
        self.click(self.take_a_picture_btn)
        self.click(self.take_a_picture_done_btn)
        self.wait_a_second()
        if self.get_elements_amount(self.message_edit_text) > 0:
            self.set_text(self.message_edit_text, 'Random text')
            self.click(self.send_button)

    @allure.step("Отправить attachment в чат")
    def check_send_attachment(self):
        self.wait_a_second()
        self.click(self.attachment_btn)
        self.wait_a_second()
        self.click(self.d(resourceId="com.yapmap.yapmap:id/button", text="Select from gallery"))
        # self.permission.photo_permission_allow()
        self.click(self.get_random_element('//android.widget.ImageView[@resource-id="com.yapmap.yapmap:id/picture_view"]'))
        self.click(self.attachment_btn)
        self.click(self.d(resourceId="com.yapmap.yapmap:id/button", text="Select from files"))
        self.wait_element('//android.widget.TextView[@resource-id="com.google.android.documentsui:id/header_title"]') #recent files title
        self.click(self.get_random_element('//*[@resource-id="com.google.android.documentsui:id/dir_list"]/android.widget.LinearLayout'))

    @allure.step("Открытие моих заметок")
    def open_my_notes(self):
        self.click(self.my_notes, 'My notes')

    @allure.step("Свайп по горизонтальному меню")
    def swipe_horizontal_menu(self):
        fx, fy = self.get_element(self.menu_tabs).center()
        tx = 50
        ty = fy
        self.swipe_coordinate(fx, fy, tx, ty)

    @allure.step("Свайп по горизонтальни к элементу")
    def swipe_horizontal_to_element(self, locator):
        for i in range(3):
            if self.get_elements_amount(locator) == 0:
                self.swipe_horizontal_menu()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break

    @allure.step("Открыть таб People")
    def open_people_tab(self):
        self.click('//*[@content-desc="People"]')

    @allure.step("Открыть таб Events")
    def open_events_tab(self):
        self.click('//*[@content-desc="Events"]')

    @allure.step("Открыть таб Groups")
    def open_groups_tab(self):
        self.click('//*[@content-desc="Groups"]')

    @allure.step("Открыть таб Businesses")
    def open_businesses_tab(self):
        self.wait_a_second()
        self.click('//*[@content-desc="Businesses"]')
        self.wait_a_second()

    @allure.step("Открыть таб Market")
    def open_market_tab(self):
        self.swipe_horizontal_to_element('//*[@content-desc="Market"]')
        self.wait_a_second()
        self.click('//*[@content-desc="Market"]')

    @allure.step("Открыть таб Jobs")
    def open_jobs_tab(self):
        self.swipe_horizontal_to_element('//*[@content-desc="Jobs"]')
        self.wait_a_second()
        self.click('//*[@content-desc="Jobs"]')

    @allure.step("Открыть таб Pets")
    def open_pets_tab(self):
        self.swipe_horizontal_to_element('//*[@content-desc="Pets"]')
        self.wait_a_second()
        self.click('//*[@content-desc="Pets"]')

    @allure.step("Открыть таб Places")
    def open_places_tab(self):
        self.swipe_horizontal_to_element('//*[@content-desc="Places"]')
        self.wait_a_second()
        self.click('//*[@content-desc="Places"]')

    @allure.step("Проверяем отправку текстового сообщения в чат")
    def check_send_text(self):
        message = faker.text()
        self.send_message(message)
        self.wait_text(message)
        return message

    @allure.step("Выход из чата")
    def back_from_chat_to_main(self):
        self.click(self.back_btn_2, 'кнопка <-')
        self.wait_a_second()
        self.click_back_btn()
        self.wait_a_second()

    @allure.step("Выход из чата")
    def back_from_chat(self):
        self.click(self.back_btn_2, 'кнопка <-')
        self.wait_a_second()

    @allure.step("Отправка в чат сообщения '{message}'")
    def send_message(self, message):
        self.set_text(self.message_field, message, "сообщение")
        self.click(self.send_message_btn, "кнопка отправки сообщения")
        self.wait_a_second()

    @allure.step("Проверка комментария к сообщению")
    def checking_comment(self):
        self.wait_element(self.comment_button)
        self.click(self.comment_button, 'кнопка Comment')
        self.wait_element(self.bottom_sheet_title)
        self.wait_text('Comments')
        comment = faker.text()
        self.send_message(comment)
        self.wait_text('Discussion started')
        return comment

    @allure.step("Открыть объект по имени")
    def open_item_by_name(self, name_item):
        item = f'//*[@text="{name_item}"]'
        self.swipe_down_to_element(item)
        self.wait_a_second()
        self.click(item)

    @allure.step("Проверка пустого экрана чата")
    def checking_clear_chat(self):
        self.open_people_tab()
        # self.wait_element(self.find_button)
        self.wait_text("My notes")

        self.open_events_tab()
        self.wait_element(self.create_event_button)

        self.open_groups_tab()
        self.wait_element(self.create_group_button)

        self.open_businesses_tab()
        self.click(self.i_own)

        self.open_market_tab()
        self.click(self.i_own)

        self.open_jobs_tab()
        self.click(self.i_own)

        self.open_pets_tab()
        self.click(self.i_own)

        self.open_places_tab()
        self.click(self.i_own)

    @allure.step("Проверка сообщения в чате")
    def check_message_in_chat(self, message):
        self.wait_a_second()
        self.wait_text(message)

