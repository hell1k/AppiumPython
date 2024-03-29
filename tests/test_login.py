import time

import allure
import pytest
import uiautomator2 as u
from selenium import webdriver

from pages.base_page import BasePage

d = u.connect("emulator-5554")


@pytest.mark.usefixtures("setup")
class TestExample:

    @allure.title("Редактирование имени пользователя")
    @pytest.mark.smoke
    def test_edit_profile(self, authorization):
        self.menu.open_profile()
        self.profile.edit_profile_fields()

    @allure.title("Редактирование полей профиля")
    @pytest.mark.smoke
    def test_edit_profile_data(self, authorization):
        self.menu.open_profile()
        self.profile.click_edit_profile()
        profile_data = self.profile.edit_profile()
        self.profile.click_edit_profile()
        self.profile.check_data_name(profile_data[0])
        self.profile.check_data_name(profile_data[1])
        self.profile.check_data_name(profile_data[2])
        self.profile.swipe_up()
        self.profile.check_data_name(profile_data[3])
        self.profile.check_data_name(profile_data[4])

    @allure.title("Отмена редактирования")
    @pytest.mark.smoke
    def test_checking_undoing_changes(self, authorization):
        self.menu.open_profile()
        self.profile.canceling_changes()

    @allure.title("Регистрация нового пользователя")
    @pytest.mark.smoke
    @pytest.mark.registration
    def test_registration(self):
        new_first_name, new_last_name, status, orientation, religion, ethnos, height, weight, country, phone, mail = self.login.registration()
        self.profile.checking_registration_data(new_first_name, new_last_name, status, orientation, religion, ethnos,
                                                height, weight, country, phone, mail)

    @allure.title("Проверка данных в полях профиля")
    @pytest.mark.smoke
    def test_profile_data_fields(self, authorization):
        self.menu.open_profile()
        self.profile.click_edit_profile()
        self.profile.checking_first_name_length()
        self.profile.checking_last_name_length()
        self.profile.checking_data_fields('Gender', ('Male', 'Female'))
        self.profile.checking_data_fields('Status', ('Single', 'Married', 'Divorced', 'Widowed', 'Complicated'))
        self.profile.swipe_up()
        self.profile.checking_data_fields('Sexual orientation', ('Hetero', 'Bi', 'Homo'))
        self.profile.checking_data_fields('Religion', ('Christianity', 'Islam', 'Atheist', 'Hinduism', 'Buddhism',
                                                       'Chinese traditional religion', 'Ethnic religion',
                                                       'African traditional religions', 'Sikhism', 'Spiritism',
                                                       'Judaism', "Bahá'í", 'Jainism', 'Shinto', 'Cao Dai',
                                                       'Zoroastrianism', 'Tenrikyo', 'Neo-Paganism',
                                                       'Unitarian Universalism', 'Rastafari', 'Esoteric', 'Other'))
        self.profile.checking_data_fields('Ethnos', ('European', 'Black', 'Asian', 'American/red race',
                                                     'Caucasian race/white race', 'Malayan/brown race',
                                                     'Ethiopid/black race', 'Mongolian/yellow race'))
        self.profile.checking_data_fields('Status', ('Single', 'Married', 'Divorced', 'Widowed', 'Complicated'))


def test_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-US")
    driver = webdriver.Chrome(options=options)
    driver.get("https://ya.ru")
    time.sleep(1)
    allure.attach(
        name="Скриншот",
        body=driver.get_screenshot_as_png(),
        attachment_type=allure.attachment_type.PNG,
    )
    print(driver.title)
    driver.close()


def test_install(install_app):
    print("qq")
