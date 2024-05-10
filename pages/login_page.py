import random
import re
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from common.menu import Menu
from common.permission import Permission
from pages.profile_page import ProfilePage
from faker import Faker

faker = Faker()


class LoginPage(BasePage):
    menu = Menu()
    profile = ProfilePage()
    permission = Permission()

    sign_in_btn = "com.yapmap.yapmap:id/sign_in_button"
    sign_up_btn = "com.yapmap.yapmap:id/sign_up_button"
    email_field = '//*[@resource-id="com.yapmap.yapmap:id/email_edit_text_layout"]/android.widget.FrameLayout[1]'
    password_field = '//*[@resource-id="com.yapmap.yapmap:id/password_edit_text_layout"]/android.widget.FrameLayout[1]'
    confirm_password_field = '//*[@resource-id="com.yapmap.yapmap:id/confirm_password_edit_text_layout"]/android.widget.FrameLayout[1]'
    terms_switch = '//*[@resource-id="com.yapmap.yapmap:id/terms_switch"]'
    code_first_number = '//*[@resource-id="com.yapmap.yapmap:id/first_input_layout"]/android.widget.FrameLayout[1]'
    code_second_number = '//*[@resource-id="com.yapmap.yapmap:id/second_input_layout"]/android.widget.FrameLayout[1]'
    code_third_number = '//*[@resource-id="com.yapmap.yapmap:id/third_input_layout"]/android.widget.FrameLayout[1]'
    code_fourth_number = '//*[@resource-id="com.yapmap.yapmap:id/fourth_input_layout"]/android.widget.FrameLayout[1]'
    new_account_title = 'com.yapmap.yapmap:id/new_account_text_view'
    personal_info_title = 'com.yapmap.yapmap:id/personal_info_text_view'
    phone_number_title = '//*[@text="Phone number"]'
    first_name_field = '//*[@resource-id="com.yapmap.yapmap:id/first_name_layout"]'
    last_name_field = '//*[@resource-id="com.yapmap.yapmap:id/last_name_layout"]'
    date_field = '//*[@resource-id="com.yapmap.yapmap:id/dob_text_view"]'
    prev_month = '//*[@resource-id="android:id/prev"]'
    date_ok = '//*[@resource-id="android:id/button1"]'
    date_year_btn = '//*[@resource-id="android:id/date_picker_header_year"]'
    date_year_selector = '//*[@resource-id="android:id/text1"]'
    male_btn = '//*[@resource-id="com.yapmap.yapmap:id/male_text_view"]'
    female_btn = '//*[@resource-id="com.yapmap.yapmap:id/female_text_view"]'
    continue_btn = '//*[@resource-id="com.yapmap.yapmap:id/continue_button"]'
    profile_photo = '//*[@resource-id="com.yapmap.yapmap:id/profile_photo_layout"]/android.widget.FrameLayout[1]'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    country_field = '//*[@resource-id="com.yapmap.yapmap:id/country_text_view"]'
    countries_list = 'android:id/text1'
    phone_fields = '//*[@resource-id="com.yapmap.yapmap:id/phone_edit_text"]'
    next_btn = '//*[@resource-id="com.yapmap.yapmap:id/action_next"]'
    logout_btn = 'com.yapmap.yapmap:id/logout_button'
    logout_alert = 'com.yapmap.yapmap:id/alertTitle'
    confirmation_logout_btn = '//*[@resource-id="android:id/button1"]'
    cancel_logout_btn = '//*[@resource-id="android:id/button2"]'

    @allure.step("Авторизация")
    def authorization(self, email=None, password=None):
        self.click_sign_in()
        if email is not None and password is not None:
            self.set_text(self.email_field, email, "поле Почта")
            self.set_text(self.password_field, password, "поле Пароль")
        else:
            self.set_text(self.email_field, 'hell1k@yandex.ru', "поле Почта")
            self.set_text(self.password_field, '12345678Qq!', "поле Пароль")
        self.click_sign_in()

    @allure.step("Авторизация")
    def login(self, email=None, password=None):
        self.click_sign_in()
        if email is not None and password is not None:
            self.set_text(self.email_field, email, "поле Почта")
            self.set_text(self.password_field, password, "поле Пароль")
        else:
            self.set_text(self.email_field, 'idgwynbleidd@gmail.com', "поле Почта")
            self.set_text(self.password_field, 'Qq12345678!', "поле Пароль")
        self.click_sign_in()

    @allure.step("Клик по кнопке Регистрация")
    def click_sign_up(self):
        self.click(self.sign_up_btn, 'sign up')

    @allure.step("Клик по кнопке Авторизация")
    def click_sign_in(self):
        self.click(self.sign_in_btn, 'sign in')

    @allure.step("Регистрация")
    def registration(self):
        self.click_sign_up()
        with allure.step("1 step"):
            user_name = "test" + str(random.randint(0, 99999999))
            mail = user_name + "@mailforspam.com"
            self.set_text(self.email_field, mail, "поле Email")
            self.set_text(self.password_field, "Qq12345678!", "поле Password")
            self.set_text(self.confirm_password_field, "Qq12345678!", "поле Confirm password")
            self.click(self.terms_switch, "Terms of use")
            self.click_sign_up()
            self.wait_a_second()
            self.wait_a_second()
            self.set_verification_code(user_name)
            self.wait_a_second()
        with allure.step("2 step"):
            self.wait_element(self.new_account_title)
            self.set_photo()
            new_first_name = faker.first_name()
            new_last_name = faker.last_name()
            self.set_text(self.first_name_field, new_first_name, 'First name')
            self.set_text(self.last_name_field, new_last_name, 'Last name')
            self.set_date()
            self.set_gender()
            self.swipe_up()
            self.click(self.continue_btn, "кнопка Continue")
        with allure.step("3 step"):
            self.wait_element(self.personal_info_title, "заголовок User's personal information")
            status = self.profile.edit_profile_data("Status")
            orientation = self.profile.edit_profile_data("Sexual orientation")
            religion = self.profile.edit_profile_data("Religion")
            ethnos = self.profile.edit_profile_data("Ethnos")
            self.swipe_up()
            height = str(150 + random.randint(1, 50))
            weight = str(50 + random.randint(1, 50))
            self.profile.edit_height(height)
            self.profile.edit_weight(weight)
            self.click(self.continue_btn, "кнопка Continue")
        with allure.step("4 step"):
            self.wait_element(self.phone_number_title, "заголовок Phone number")
            country = self.set_country()
            phone = self.set_phone()
            self.click(self.next_btn, "кнопка Next")
        self.permission.click_while_using_the_app()
        self.wait_a_second()
        return new_first_name, new_last_name, status, orientation, religion, ethnos, height, weight, country, phone, mail

    @allure.step("Выбор значения в поле Страна")
    def set_country(self):
        self.click(self.country_field, "поле Country")
        country_element = self.get_random_element(self.countries_list)
        country_name = country_element.get_text()
        self.click(country_element, country_name)
        return country_name

    @allure.step("Выбор значения в поле Телефон")
    def set_phone(self):
        phone_number = str(random.randint(1000000000, 9999999999))
        self.set_text(self.phone_fields, phone_number, 'Phone number}')
        return phone_number

    @allure.step("Выбор значения в поле Фото")
    def set_photo(self):
        self.click(self.profile_photo, "поле Photo")
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "подтверждение созданного фото")

    @allure.step("Получение и установка проверочного кода")
    def set_verification_code(self, user_name):
        time.sleep(10)
        code = str(self.get_verification_code(user_name))
        self.set_text(self.code_first_number, code[0])
        self.set_text(self.code_second_number, code[1])
        self.set_text(self.code_third_number, code[2])
        self.set_text(self.code_fourth_number, code[3])

    @allure.step("Выбор значения в поле Пол")
    def set_gender(self):
        random_number = random.randint(0, 1)
        if random_number == 0:
            self.click(self.male_btn, "male")
        else:
            self.click(self.female_btn, "female")

    @allure.step("Выбор значения в поле Дата")
    def set_date(self):
        self.click(self.date_field, "поле Дата")
        self.click(self.date_year_btn, "переход к выбору года")
        self.click(self.date_year_selector, "год")
        random_date = random.randrange(1, 29)
        self.click(f'//*[@text={str(random_date)}]', f'дата {random_date}')
        self.click(self.date_ok, "кнопка Ок")

    def get_verification_code(self, user_name):
        options = webdriver.FirefoxOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        options.add_argument("--lang=en-US")
        driver = webdriver.Firefox(options=options)
        driver.get(f"https://www.mailforspam.com/mail/{user_name}/1")
        code_value = int(re.sub('[^0-9]', "", driver.find_element(By.XPATH,
                                                                  "//span[contains(text(), 'Your YapMapApp verification code is:')]").text))
        driver.close()
        return code_value

    @allure.step("Логаут")
    def logout(self):
        self.menu.open_profile()
        self.swipe_to_element(self.logout_btn)
        self.wait_a_second()
        self.click(self.logout_btn, "кнопка Log out")
        self.wait_element(self.logout_alert, "logout alert")
        self.click(self.confirmation_logout_btn, "кнопка подтверждения выхода")
        self.wait_element(self.sign_in_btn)
