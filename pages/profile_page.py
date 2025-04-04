import random

import allure
import pytest
from faker import Faker

from pages.base_page import BasePage
from common.menu import Menu

faker = Faker()


class ProfilePage(BasePage):
    menu = Menu()

    edit_profile_icon = "com.yapmap.yapmap:id/edit_view"
    first_name_field = '//*[@resource-id="com.yapmap.yapmap:id/first_name_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    last_name_field = '//*[@resource-id="com.yapmap.yapmap:id/last_name_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    nickname_field = '//*[@resource-id="com.yapmap.yapmap:id/nickname_field"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
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
    back_btn = '//*[@resource-id="com.yapmap.yapmap:id/toolbar"]//android.widget.ImageButton'
    unsaved_changes_notification = '//*[@resource-id="com.yapmap.yapmap:id/title_text_view" and @text="Unsaved changes"]'
    cancel_changes_btn = '//*[@resource-id="com.yapmap.yapmap:id/action_button" and @text="CANCEL"]'
    no_changes_btn = '//*[@resource-id="com.yapmap.yapmap:id/action_accented_button" and @text="NO"]'
    yes_changes_btn = '//*[@resource-id="com.yapmap.yapmap:id/action_accented_button" and @text="YES"]'
    phone_field = '//*[@resource-id="com.yapmap.yapmap:id/phone_field"]'
    email_field = '//*[@resource-id="com.yapmap.yapmap:id/email_field"]'
    status_orientation_view = '//*[@resource-id="com.yapmap.yapmap:id/status_orientation_text_view"]'
    first_name_error_length = '//*[@text="First Name must be no more than 50 characters"]'
    last_name_error_length = '//*[@text="Last Name must be no more than 50 characters"]'
    first_name_limit_fields = '//*[@resource-id="com.yapmap.yapmap:id/first_name_field"]//*[@resource-id="com.yapmap.yapmap:id/limit_text_view" and @text="20/20"]'
    last_name_limit_fields = '//*[@resource-id="com.yapmap.yapmap:id/last_name_field"]//*[@resource-id="com.yapmap.yapmap:id/limit_text_view" and @text="20/20"]'
    nickname_limit_fields = '//*[@resource-id="com.yapmap.yapmap:id/nickname_field"]//*[@resource-id="com.yapmap.yapmap:id/limit_text_view" and @text="20/20"]'
    group_btn_in_profile = 'com.yapmap.yapmap:id/my_groups_view'
    events_btn_in_profile = '//*[@text="Events"]'
    business_btn_in_profile = '//*[@text="Business"]'
    social_networks_btn_in_profile = '//*[@text="Social networks"]'
    purchase_history_btn_in_profile = '//*[@text="Purchase history"]'
    dating_networks_btn_in_profile = '//*[@text="Dating"]'
    market_btn_in_profile = '//*[@text="Market"]'
    pending_requests_btn_in_profile = '//*[@text="Pending requests"]'
    favorites_btn_in_profile = '//*[@text="Favorites"]'
    ads_manager_btn_in_profile = '//*[@text="Ads manager"]'
    wish_list_btn_in_profile = '//*[@text="Wish list"]'
    channels_btn_in_profile = 'com.yapmap.yapmap:id/my_channels_view'
    jobs_btn_in_profile = '//*[@text="Jobs"]'
    pets_btn_in_profile = '//*[@text="Pets"]'
    places_to_visit_btn_in_profile = '//*[@text="Places to Visit"]'
    blocked_users_btn_in_profile = '//*[@text="Blocked users"]'
    settings_btn_in_profile = '//*[@text="Settings"]'
    about_btn_in_profile = '//*[@text="About"]'
    report_a_bug_btn_in_profile = '//*[@text="Report a bug"]'
    back_btn_2 = '//*[@resource-id="com.yapmap.yapmap:id/back"]/..'

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

    @allure.step("get_profile_data_title")
    def get_profile_data_title(self, title):
        return f'//*[@text="{title}"]'

    @allure.step("Проверка наличия поля '{value}'")
    def check_data_name(self, value):
        assert self.d.xpath(f'//*[contains(@text,"{value}")]').exists == True
        self.get_screen()

    @allure.step("Редактирование роста")
    def edit_height(self, value):
        self.swipe_to_element(self.height)
        self.click(self.height, "рост")
        self.set_text(self.height_weight_field, value, 'Height')
        self.click(self.height_weight_done_btn, "кнопка Сохранить")

    @allure.step("Редактирование веса")
    def edit_weight(self, value):
        self.swipe_to_element(self.weight)
        self.click(self.weight, "вес")
        self.set_text(self.height_weight_field, value, 'Weight')
        self.click(self.height_weight_done_btn, "кнопка Сохранить")

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
            assert self.get_text(self.first_name_view) == new_first_name, "Поле First name не соответствует регистрации"
            assert self.get_text(self.last_name_view) == new_last_name, "Поле Last name не соответствует регистрации"
            assert self.get_text(self.nickname_view) == '@' + new_first_name + new_last_name, "Nickname не соответствует регистрации"
            assert status.lower() in self.get_text(
                self.status_orientation_view).lower() and orientation.lower() in self.get_text(
                self.status_orientation_view).lower(), "Статус и ориентация не соответствуют регистрации"
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
            self.swipe_to_element(self.height)
            self.check_data_name(height)
            self.swipe_to_element(self.weight)
            self.check_data_name(weight)
            self.swipe_up(3)
            self.check_data_name(phone)
            self.check_data_name(mail)
            self.check_data_name(country)

    @allure.step("Проверка наличия данных в поле '{field_name}'")
    def checking_data_fields(self, field_name, field_list):
        self.open_profile_data(field_name)
        for i in range(len(field_list)):
            self.swipe_to_element(self.get_profile_data_title(field_list[i]))
        # for i in range(len(field_list)):
        #     if len(field_list) > 10 and (i > 0 and i % 8 == 0):
        #         self.swipe_up()
        #         self.wait_a_second()
        #     self.wait_element(self.get_profile_data_title(field_list[i]), field_list[i])
        self.press_back()

    @allure.step("Проверка длины поля First name")
    def checking_first_name_length(self):
        self.set_text(self.first_name_field, faker.text(), 'long text...')
        self.wait_a_second()
        self.wait_element(self.first_name_limit_fields, "лимит 20/20")

    @allure.step("Проверка длины поля Last name")
    def checking_last_name_length(self):
        self.set_text(self.last_name_field, faker.text(), 'long text...')
        self.wait_a_second()
        self.wait_element(self.last_name_limit_fields, "лимит 20/20")

    @allure.step("Проверка длины поля Nickname")
    def checking_nickname_length(self):
        self.set_text(self.nickname_field, faker.text(), 'long text...')
        self.wait_a_second()
        self.wait_element(self.nickname_limit_fields, "лимит 20/20")

    @allure.step("Проверка переходов в разделы из Профиля")
    def checking_profile_elements(self):
        elements = ['Events', 'Business', 'Social networks', 'Purchase history', 'Dating', 'Market',
                    'Favorites', 'Wish list', 'Jobs', 'Pets', 'Places to Visit',
                    'Blocked users', 'Settings', 'About']
        for element in elements:
            self.swipe_to_element(f'//*[@text="{element}"]')
            self.click(f'//*[@text="{element}"]')
            self.wait_text(element)
            self.wait_a_second()
            self.click_back()
            self.wait_a_second()

    @allure.step("Проверка переходов в разделы из Профиля")
    def checking_profile_other_elements(self):
        self.swipe_to_element(self.group_btn_in_profile)
        self.click(self.group_btn_in_profile)
        self.wait_text('Groups')
        self.click_back()
        self.swipe_to_element(self.pending_requests_btn_in_profile)
        self.click(self.pending_requests_btn_in_profile)
        self.click(self.back_btn_2)
        self.wait_a_second()
        self.swipe_to_element(self.channels_btn_in_profile)
        self.click(self.channels_btn_in_profile)
        self.wait_text('Channels')
        self.click_back()
        self.wait_a_second()

    @allure.step("Переход в раздел Events из Профиля")
    def open_events(self):
        self.menu.open_profile()
        self.swipe_to_element(self.events_btn_in_profile)
        self.wait_a_second()
        self.click(self.events_btn_in_profile)

    @allure.step("Переход в раздел Business из Профиля")
    def open_business(self):
        self.menu.open_profile()
        self.swipe_to_element(self.business_btn_in_profile)
        self.click_business()

    @allure.step("Клик по кнопке Business")
    def click_business(self):
        self.swipe_to_element(self.business_btn_in_profile)
        self.click(self.business_btn_in_profile, "кнопка Business")
        self.wait_text("Business")
        self.wait_a_second()

    @allure.step("Открыть раздел Purchase history")
    def open_purchase_history(self):
        self.swipe_to_element(self.purchase_history_btn_in_profile)
        self.wait_a_second()
        self.click(self.purchase_history_btn_in_profile)

    @allure.step("Переход в раздел Pets из Профиля")
    def open_pets(self):
        self.menu.open_profile()
        self.swipe_to_element(self.pets_btn_in_profile)
        self.wait_a_second()
        self.click(self.pets_btn_in_profile)

    @allure.step("Клик по кнопке Jobs")
    def click_jobs(self):
        self.swipe_to_element(self.jobs_btn_in_profile)
        self.click(self.jobs_btn_in_profile, "кнопка Jobs")

    @allure.step("Переход в раздел Jobs из Профиля")
    def open_jobs(self):
        self.menu.open_profile()
        self.swipe_to_element(self.jobs_btn_in_profile)
        self.click_jobs()

    @allure.step("Переход в раздел Wish List из Профиля")
    def open_wishlist(self):
        self.menu.open_profile()
        self.swipe_to_element(self.wish_list_btn_in_profile)
        self.click(self.wish_list_btn_in_profile)

    @allure.step("Открытие раздела Market из Профиля")
    def open_market(self):
        self.menu.open_profile()
        self.swipe_to_element(self.market_btn_in_profile)
        self.wait_a_second()
        self.click(self.market_btn_in_profile)

    @allure.step("Открытие раздела Places из Профиля")
    def open_places(self):
        self.menu.open_profile()
        self.swipe_to_element(self.places_to_visit_btn_in_profile)
        self.wait_a_second()
        self.click(self.places_to_visit_btn_in_profile)

    @allure.step("Открытие раздела Favorites из Профиля")
    def open_favorites(self):
        self.menu.open_profile()
        self.swipe_to_element(self.favorites_btn_in_profile)
        self.wait_a_second()
        self.click(self.favorites_btn_in_profile)
