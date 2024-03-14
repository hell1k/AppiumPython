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
    phone_field = '//*[@resource-id="com.yapmap.yapmap:id/phone_field"]'
    email_field = '//*[@resource-id="com.yapmap.yapmap:id/email_field"]'
    status_orientation_view = '//*[@resource-id="com.yapmap.yapmap:id/status_orientation_text_view"]'
    first_name_error_length = '//*[@text="First Name must be no more than 50 characters"]'
    last_name_error_length = '//*[@text="Last Name must be no more than 50 characters"]'

    @allure.step("Редактирование данных профиля: Имя, Фамилия, Ник")
    def edit_profile_fields(self):
        self.click(self.edit_profile_icon, "иконка редактирования профиля")
        new_first_name = faker.first_name()
        new_last_name = faker.last_name()
        new_nickname = "nickname" + str(random.randint(0, 99999))
        self.set_text(self.first_name_field, new_first_name, 'First name')
        self.set_text(self.last_name_field, new_last_name, 'Last name')
        self.set_text(self.nickname_field, new_nickname, 'Nickname')
        self.click(self.save_btn, "кнопка Сохранить")
        assert self.get_text(self.first_name_view) == new_first_name
        assert self.get_text(self.last_name_view) == new_last_name
        assert self.get_text(self.nickname_view) == '@' + new_nickname

    @allure.step("Редактирование имени")
    def edit_first_name(self):
        new_first_name = faker.first_name()
        self.set_text(self.first_name_field, new_first_name, 'First name')

    @allure.step("Отмена редактирования")
    def canceling_changes(self):
        first_name = self.get_text(self.first_name_view)
        self.click_edit_profile()
        self.edit_first_name()
        self.click_back()
        self.wait_a_moment()
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
        self.wait_a_moment()

    @allure.step(
        "Редактирование данных профиля: Date, Gender, Status, Sexual orientation, Religion, Ethnos, Height, Weight")
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
        self.swipe_up()
        ethnos = self.edit_profile_data('Ethnos')
        self.check_data_name(ethnos)
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
        self.click(self.get_element(self.profile_data_value)[counter], data_name)
        return data_name

    @allure.step("Открытие поля '{title}'")
    def open_profile_data(self, title):
        self.click(self.get_profile_data_title(title), title)
        self.wait_a_second()

    def get_profile_data_title(self, title):
        return f'//*[@text="{title}"]'

    @allure.step("Проверка наличия поля '{value}'")
    def check_data_name(self, value):
        assert self.d.xpath(f'//*[contains(@text,"{value}")]').exists == True
        self.get_screen()

    @allure.step("Редактирование роста")
    def edit_height(self, value):
        self.click(self.height, "рост")
        self.set_text(self.height_weight_field, value, 'Height')
        self.click(self.height_weight_done_btn, "кнопка Сохранить")

    @allure.step("Редактирование веса")
    def edit_weight(self, value):
        self.click(self.weight, "вес")
        self.set_text(self.height_weight_field, value, 'Weight')
        self.click(self.height_weight_done_btn, "кнопка Сохранить")

    def load_photo(self):
        self.d(resourceId="com.yapmap.yapmap:id/photos_field_add_photo_text_view").send_keys(
            "/home/el_erizo/Загрузки/AppiumPython/screen.png")
        Permission().close_photo_permission()

    @allure.step("Редактирование даты")
    def edit_date(self):
        self.click(self.date_field, "поле Дата")
        random_date = random.randrange(1, 29)
        self.click(f'//*[@text={str(random_date)}]', f'дата {random_date}')
        self.click(self.date_ok, "кнопка Ок")

    @allure.step("Проверка данных после регистрации")
    def checking_registration_data(self, new_first_name, new_last_name, status, orientation, religion, ethnos, height,
                                   weight, country, phone, mail):
        with allure.step("Проверка данных в шапке профиля: First name, Last name, Nickname, status/orientation"):
            self.menu.open_profile()
            assert self.get_text(self.first_name_view) == new_first_name, print(
                "Поле First name не соответствует регистрации")
            assert self.get_text(self.last_name_view) == new_last_name, print(
                "Поле Last name не соответствует регистрации")
            assert self.get_text(self.nickname_view) == '@' + new_first_name + new_last_name, print(
                "Nickname не соответствует регистрации")
            assert status.lower() in self.get_text(
                self.status_orientation_view).lower() and orientation.lower() in self.get_text(
                self.status_orientation_view).lower(), print("Статус и ориентация не соответствуют регистрации")
        with allure.step("Проверка данных профиля"):
            self.click_edit_profile()
            self.check_data_name(new_first_name)
            self.check_data_name(new_last_name)
            self.check_data_name(new_first_name + new_last_name)
            self.swipe_up()
            self.check_data_name(status)
            self.check_data_name(orientation)
            self.check_data_name(religion)
            self.check_data_name(ethnos)
            self.swipe_up()
            self.check_data_name(height)
            self.check_data_name(weight)
            self.swipe_up()
            self.swipe_up()
            self.swipe_up()
            self.check_data_name(phone)
            self.check_data_name(mail)
            self.check_data_name(country)

    @allure.step("Проверка наличия данных в поле '{field_name}'")
    def checking_data_fields(self, field_name, field_list):
        self.open_profile_data(field_name)
        for i in range(len(field_list)):
            if len(field_list) > 10 and i > 0 and i % 4 == 0:
                self.swipe_up()
                self.wait_a_second()
            self.checking_exists_element(self.get_profile_data_title(field_list[i]), field_list[i])
        self.press_back()

    @allure.step("Проверка длины поля First name")
    def checking_first_name_length(self):
        self.set_text(self.first_name_field, faker.text(), 'long text...')
        self.wait_a_second()
        self.checking_exists_element(self.first_name_error_length, "ошибка длины поля First name")

    @allure.step("Проверка длины поля Last name")
    def checking_last_name_length(self):
        self.set_text(self.last_name_field, faker.text(), 'long text...')
        self.wait_a_second()
        self.checking_exists_element(self.last_name_error_length, "ошибка длины поля Last name")
