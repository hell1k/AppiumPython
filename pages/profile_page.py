import random
import time

import allure
from faker import Faker

from pages.base_page import BasePage
from pages.menu import Menu
from pages.permission import Permission

faker = Faker()


class ProfilePage(BasePage):
    menu = Menu()

    edit_profile_icon = "com.yapmap.yapmap:id/edit_view"
    first_name_field = '//*[@resource-id="com.yapmap.yapmap:id/first_name_field"]'
    last_name_field = '//*[@resource-id="com.yapmap.yapmap:id/last_name_field"]'
    nickname_field = '//*[@resource-id="com.yapmap.yapmap:id/nickname_field"]'
    save_btn = "com.yapmap.yapmap:id/action_show_option_menu"
    first_name_view = "com.yapmap.yapmap:id/first_name_text_view"
    last_name_view = "com.yapmap.yapmap:id/last_name_text_view"
    nickname_view = "com.yapmap.yapmap:id/nickname_text_view"
    height = '//*[@text="Height"]'
    weight = '//*[@text="Weight"]'
    height_weight_field = '//*[@resource-id="com.yapmap.yapmap:id/container"]'
    height_weight_done_btn = '//*[@resource-id="com.yapmap.yapmap:id/done_button"]'
    profile_data_value = "com.yapmap.yapmap:id/value_text_view"

    def edit_profile_fields(self):
        self.click(self.edit_profile_icon)
        new_first_name = faker.first_name()
        new_last_name = faker.last_name()
        new_nickname = "nickname" + str(random.randint(0, 99999))
        self.set_text(self.first_name_field, new_first_name)
        self.set_text(self.last_name_field, new_last_name)
        self.set_text(self.nickname_field, new_nickname)
        self.click(self.save_btn)
        assert self.get_text(self.first_name_view) == new_first_name
        assert self.get_text(self.last_name_view) == new_last_name
        assert self.get_text(self.nickname_view) == '@' + new_nickname

    @allure.step("Клик по кнопке редактирования профиля")
    def click_edit_profile(self):
        self.click(self.edit_profile_icon)

    def edit_profile(self):
        gender = self.edit_profile_data('Gender')
        self.check_data_name(gender)
        status = self.edit_profile_data('Status')
        self.check_data_name(status)
        orientation = self.edit_profile_data('Sexual orientation')
        self.check_data_name(orientation)
        religion = self.edit_profile_data('Religion')
        self.check_data_name(religion)
        ethnos = self.edit_profile_data('Ethnos')
        self.check_data_name(ethnos)
        self.swipe_down()
        self.swipe_down()
        height = "180"
        weight = "80"
        self.edit_height(height)
        self.edit_weight(weight)
        self.click(self.save_btn)
        return gender, status, orientation, religion, ethnos, height, weight

    @allure.step("Редактирование '{title}'")
    def edit_profile_data(self, title):
        self.click(self.get_profile_data_title(title))
        self.wait_a_second()
        counter = random.randrange(0, self.get_element(self.profile_data_value).count)
        data_name = self.get_element(self.profile_data_value)[counter].get_text()
        self.get_element(self.profile_data_value)[counter].click()
        return data_name

    def get_profile_data_title(self, title):
        return f'//*[@text="{title}"]'

    @allure.step("Проверка наличия поля '{value}'")
    def check_data_name(self, value):
        assert self.d.xpath(f'//*[@text="{value}"]').exists == True
        self.get_screen()

    def edit_height(self, value):
        self.click(self.height)
        self.set_text(self.height_weight_field, value)
        self.click(self.height_weight_done_btn)

    def edit_weight(self, value):
        self.click(self.weight)
        self.set_text(self.height_weight_field, value)
        self.click(self.height_weight_done_btn)

    def load_photo(self):
        self.d(resourceId="com.yapmap.yapmap:id/photos_field_add_photo_text_view").send_keys("/home/el_erizo/Загрузки/AppiumPython/screen.png")
        Permission().close_photo_permission()