import random

import allure
import faker
from faker import Faker
from common.menu import Menu
from common.photo import Photo
from common.permission import Permission
from pages.base_page import BasePage
from tests.config import *


class FavoritesPage(BasePage):
    menu = Menu()
    photo = Photo()
    faker = Faker()

    edit_btn = "com.yapmap.yapmap:id/action_edit"
    cancel_button = "com.yapmap.yapmap:id/cancel_button"
    delete_button = "com.yapmap.yapmap:id/delete_button"
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    plus_btn = "com.yapmap.yapmap:id/action_show_option_menu"
    add_picture_btn = "com.yapmap.yapmap:id/no_image_layout"
    name_wish = '//*[@text="Wishes"]'
    link_wish = '//*[@text="Link to product in the store"]'
    description = '//*[@resource-id="com.yapmap.yapmap:id/description_input_edit_text_field"]'
    add_photos_btn = '//*[@resource-id="com.yapmap.yapmap:id/photos_field_add_photo_text_view"]'
    create_btn = '//*[@resource-id="com.yapmap.yapmap:id/create_button"]'
    add_extra_pictures_check_box = '//*[@resource-id="com.yapmap.yapmap:id/add_extra_pictures_check_box"]'
    more_options = '//*[@resource-id="com.yapmap.yapmap:id/action_show_option_menu"]'
    edit_image_btn = '//*[@resource-id="com.yapmap.yapmap:id/circle_2_view"]'
    share_button = '//*[@resource-id="com.yapmap.yapmap:id/share_button"]'
    ok_button = '//*[@resource-id="com.yapmap.yapmap:id/ok_button"]'

    def open_item(self, name):
        self.swipe_to_element(f'//*[@text="{name}"]/..')
        self.click(f'//*[@text="{name}"]/..')

    @allure.step("Проверяем имя")
    def check_name(self, name):
        self.wait_a_second()
        self.swipe_to_element(f'//*[@text="{name}"]/..')
        self.wait_a_second()
        self.wait_text(name)

    def click_edit(self):
        self.click(self.edit_btn, 'кнопка Редактировать (карандаш в верхнем правом углу)')
        self.wait_a_moment()

    @allure.step("Проверяем цвет иконки добавления в избранное")
    def favorite_btn_wait_color(self):
        counter = 15
        while counter > 0:
            color = self.get_color_element(self.add_to_favorites_btn)
            if color == (175, 144, 255) or color == (175, 144, 255, 255) or color == (174, 145, 255):
                break
            else:
                self.wait_a_second()
                counter = counter - 1
        else:
            color = self.get_color_element(self.add_to_favorites_btn)
            assert color == (175, 144, 255) or color == (174, 145, 255), f'Цвет иконки {color}, а должен быть (175, 144, 255) или (174, 145, 255)'

    def create_wishlist(self):
        self.click(self.plus_btn, 'Кнопка +')
        self.wait_text('Create your wish')
        self.click(self.add_picture_btn, 'кнопка Add one picture')
        self.photo.upload_picture()
        wish_name = 'Test wish_' + str(random.randint(0, 999999999))
        self.set_text(self.name_wish, wish_name)
        self.set_text(self.link_wish, 'https://clck.ru/3BKwaY')
        self.set_text(self.description, text_250)
        self.swipe_to_element(self.add_extra_pictures_check_box)
        self.click(self.add_extra_pictures_check_box, 'чекбокс Add extra pictures')
        self.click(self.add_photos_btn, 'кнопка Add photos')
        self.wait_text('Selected 0 of 5')
        self.press_back()
        self.click(self.add_extra_pictures_check_box, 'чекбокс Add extra pictures')
        self.swipe_to_element(self.create_btn)
        self.click(self.create_btn, 'кнопка Create')
        self.wait_text('Wish list')

    def open_wishlist(self):
        self.click('//*[@resource-id="com.yapmap.yapmap:id/items_recycler_view"]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]')

    @allure.step("Переход в доп опции ... '{option_name}'")
    def open_more_options(self, option_name):
        self.click(self.more_options, "меню ...")
        self.click(f'//*[@text="{option_name}"]', option_name)

    @allure.step("Переход к доп опциям изображения")
    def open_images_options(self, option_name):
        self.click(self.edit_image_btn)
        self.click(f'//*[@text="{option_name}"]', option_name)

    @allure.step("Проверка меню ... в шапке")
    def checking_more_options(self):
        self.wait_a_moment()
        self.open_more_options('Edit')
        self.wait_text('Update your wish')
        self.open_images_options('Cancel')

        self.open_images_options('Pick photo')
        self.photo.upload_picture(permission=False)

        self.open_images_options('Remove')


        self.wait_text('Update your wish')
        self.click(self.add_picture_btn, 'кнопка Add one picture')
        self.photo.upload_picture(permission=False)
        # wish_name = 'Test wish_' + str(random.randint(0, 999999999))
        # self.set_text('//*[@resource-id="com.yapmap.yapmap:id/name_input_edit_text_field"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]', wish_name)
        # self.set_text(self.link_wish, 'https://avito.ru')
        # self.set_text(self.description, text_250_2)
        # self.swipe_to_element(self.add_extra_pictures_check_box)
        # self.click(self.add_extra_pictures_check_box, 'чекбокс Add extra pictures')
        # self.click(self.add_photos_btn, 'кнопка Add photos')
        # self.wait_text('Selected 0 of 5')
        # self.press_back()
        # self.click(self.add_extra_pictures_check_box, 'чекбокс Add extra pictures')
        # self.swipe_to_element(self.create_btn)
        # self.click(self.create_btn, 'кнопка Edit')
        # self.wait_text('Wish')
        self.press_back()
        self.open_more_options('Share')
        self.wait_text('Share wish')
        self.click(self.share_button, 'кнопка SHARE')
        assert self.get_text("android:id/title") == 'Share'
        self.press_back()
        self.press_back()

        self.open_more_options('Cancel')
        self.wait_hidden_element(self.cancel_button)

        self.open_more_options('Remove')
        self.wait_text('Delete wish')
        self.click(self.ok_button, 'кнопка OK')
        self.wait_text('Wish list')

