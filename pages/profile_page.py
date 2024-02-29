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
    date_field = '//*[@resource-id="com.yapmap.yapmap:id/dob_field"]'
    date_ok = '//*[@resource-id="android:id/button1"]'
    date_cancel = '//*[@resource-id="android:id/button2"]'
    back_btn = '//*[@content-desc="Back"]'
    unsaved_changes_notification = '//*[@resource-id="com.yapmap.yapmap:id/title_text_view" and @text="Unsaved changes"]'
    cancel_changes_btn = '//*[@resource-id="com.yapmap.yapmap:id/action_button" and @text="CANCEL"]'
    no_changes_btn = '//*[@resource-id="com.yapmap.yapmap:id/action_accented_button" and @text="NO"]'
    yes_changes_btn = '//*[@resource-id="com.yapmap.yapmap:id/action_accented_button" and @text="YES"]'

    @allure.step("Редактирование данных профиля: Имя, Фамилия, Ник")
    def edit_profile_fields(self):
        self.click(self.edit_profile_icon, "иконка редактирования профиля")
        new_first_name = faker.first_name()
        new_last_name = faker.last_name()
        new_nickname = "nickname" + str(random.randint(0, 99999))
        self.set_text(self.first_name_field, new_first_name)
        self.set_text(self.last_name_field, new_last_name)
        self.set_text(self.nickname_field, new_nickname)
        self.click(self.save_btn, "кнопка Сохранить")
        assert self.get_text(self.first_name_view) == new_first_name
        assert self.get_text(self.last_name_view) == new_last_name
        assert self.get_text(self.nickname_view) == '@' + new_nickname

    @allure.step("Редактирование имени")
    def edit_first_name(self):
        new_first_name = faker.first_name()
        self.set_text(self.first_name_field, new_first_name)

    @allure.step("Отмена редактирования")
    def canceling_changes(self):
        first_name = self.get_text(self.first_name_view)
        self.click_edit_profile()
        self.edit_first_name()
        self.click_back()
        self.wait_a_second()
        self.wait_element(self.unsaved_changes_notification, "уведомление об отмене редактирования")
        self.click(self.no_changes_btn, "кнопка отмены сохранения")
        self.wait_a_moment()
        assert self.get_text(self.first_name_view) == first_name

    @allure.step("Клик по кнопке Назад")
    def click_back(self):
        self.click(self.back_btn, "кнопка Назад")

    @allure.step("Клик по кнопке редактирования профиля")
    def click_edit_profile(self):
        self.click(self.edit_profile_icon, "кнопка редактирования профиля")
        self.wait_a_second()

    @allure.step("Редактирование данных профиля: Date, Gender, Status, Sexual orientation, Religion, Ethnos, Height, Weight")
    def edit_profile(self):
        self.edit_date()
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
        self.swipe_up()
        self.swipe_up()
        height = str(150 + random.randint(1, 50))
        weight = str(50 + random.randint(1, 50))
        self.edit_height(height)
        self.edit_weight(weight)
        self.click(self.save_btn)
        return gender, status, orientation, religion, ethnos, height, weight

    @allure.step("Редактирование '{title}'")
    def edit_profile_data(self, title):
        self.click(self.get_profile_data_title(title), title)
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

    @allure.step("Редактирование роста")
    def edit_height(self, value):
        self.click(self.height, "рост")
        self.set_text(self.height_weight_field, value)
        self.click(self.height_weight_done_btn, "кнопка Сохранить")

    @allure.step("Редактирование веса")
    def edit_weight(self, value):
        self.click(self.weight, "вес")
        self.set_text(self.height_weight_field, value)
        self.click(self.height_weight_done_btn, "кнопка Сохранить")

    def load_photo(self):
        self.d(resourceId="com.yapmap.yapmap:id/photos_field_add_photo_text_view").send_keys(
            "/home/el_erizo/Загрузки/AppiumPython/screen.png")
        Permission().close_photo_permission()

    @allure.step("Редактирование даты")
    def edit_date(self):
        self.click(self.date_field, "поле Дата")
        random_date = random.randrange(1, 29)
        self.click(self.d.xpath(f'//*[@text={str(random_date)}]'), f'дата {random_date}')
        self.click(self.date_ok, "кнопка Ок")
