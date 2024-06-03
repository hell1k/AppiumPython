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

    def click_people_tab(self):
        self.click(self.people_tab, 'вкладка People')

    def click_pets_tab(self):
        self.swipe_to_element_in_tab(self.pets_tab)
        self.click(self.pets_tab, 'вкладка Pets')

    def click_market_tab(self):
        self.swipe_to_element_in_tab(self.market_tab)
        self.click(self.market_tab, 'вкладка Market')

    def click_business_tab(self):
        self.wait_a_second()
        self.wait_a_second()
        self.swipe_to_element_in_tab(self.business_tab)
        self.click(self.business_tab, 'вкладка Business')

    def click_jobs_tab(self):
        self.swipe_to_element_in_tab(self.jobs_tab)
        self.click(self.jobs_tab, 'вкладка Jobs')

    @allure.step("Проверяем чат раздела Pets")
    def check_pets_message(self, pet_name, user_pet_name, message):
        self.click_pets_tab()
        self.click(self.i_own)
        self.click(f'//*[@text="{pet_name}"]', pet_name)
        self.wait_a_second()
        self.click(f'//*[@text="{user_pet_name}"]', user_pet_name)
        self.wait_a_second()
        self.wait_text(message)

    def swipe_horizontal_tabs(self):
        fx, fy = self.get_element(self.tab_layout).center()
        tx, ty = self.get_element(self.people_tab).center()
        self.swipe_coordinate(fx, fy, tx, ty)

    def swipe_to_element_in_tab(self, locator):
        for i in range(3):
            if self.get_elements_amount(locator) == 0:
                self.swipe_horizontal_tabs()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break

    @allure.step("Проверяем чат раздела Business")
    def check_business_message(self, business_name, new_message):
        self.click_business_tab()
        self.click(self.i_own)
        self.click(self.business_chats)
        self.wait_text(business_name)
        self.wait_a_second()
        self.wait_text(new_message)

    @allure.step("Проверяем чат раздела Job")
    def check_job_message(self, position_name, message):
        self.click_jobs_tab()
        self.click(self.i_own)
        self.click(f'//*[@text="{position_name}"]', position_name)
        self.wait_a_second()
        self.wait_text(message)

    @allure.step("Проверяем чат раздела Market")
    def check_market_message(self, message):
        self.click_market_tab()
        self.click(self.i_own)
        self.wait_text(message)
        self.click(f'//*[@text="{message}"]')
        self.wait_text(message)

    @allure.step("Отправить emoji в чат")
    def check_send_emoji(self):
        self.click(self.emoji_btn, 'кнопка Emoji')
        self.click(self.get_random_element(self.emoji_list), 'рандомный emoji')
        self.click(self.send_button)

    @allure.step("Отправить sticker в чат")
    def check_send_sticker(self):
        self.click(self.stickers_btn, 'кнопка Sticker')
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
        self.click(self.stickers_btn, 'кнопка Sticker')
        self.click('//*[@resource-id="com.yapmap.yapmap:id/icons_recycler_view"]/android.widget.LinearLayout[3]')


        # self.click(
        #     self.d('//*[@resource-id="com.yapmap.yapmap:id/icons_recycler_view"]/android.widget.LinearLayout[2]'))
        # self.wait_text('Upload your stickers now!')

    @allure.step("Отправить images в чат")
    def check_send_images(self):
        self.click(self.images_btn)
        self.click(self.d(resourceId="com.google.android.documentsui:id/sub_menu"))
        self.click(self.get_random_element('//*[@resource-id="com.google.android.documentsui:id/dir_list"]/android.widget.LinearLayout'))
        self.set_text(self.message_edit_text, 'Random text')
        self.click(self.send_button)

    @allure.step("Отправить images с камеры в чат")
    def check_send_images_from_camera(self):
        self.click(self.camera_btn)
        self.permission.click_while_using_the_app()
        self.click(self.take_a_picture_btn)
        self.click(self.take_a_picture_done_btn)
        self.set_text(self.message_edit_text, 'Random text')
        self.click(self.send_button)

    @allure.step("Отправить attachment в чат")
    def check_send_attachment(self):
        self.click(self.attachment_btn)
        self.click(self.d(resourceId="com.yapmap.yapmap:id/button", text="Select from gallery"))
        # self.permission.photo_permission_allow()
        self.click(self.get_random_element('//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup'))
        self.click(self.attachment_btn)
        self.click(self.d(resourceId="com.yapmap.yapmap:id/button", text="Select from files"))
        self.click(self.get_random_element('//*[@resource-id="com.google.android.documentsui:id/dir_list"]/android.widget.LinearLayout'))
