import time

import allure
import pytest
import uiautomator2 as u
from selenium import webdriver

d = u.connect("emulator-5554")


@pytest.mark.usefixtures("setup")
@allure.feature("Профиль")
class TestProfile:

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
    @pytest.mark.profile
    def test_profile_data_fields(self, authorization):
        self.menu.open_profile()
        self.profile.click_edit_profile()
        self.profile.checking_first_name_length()
        self.profile.checking_last_name_length()
        self.profile.checking_nickname_length()
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

    @allure.title("Проверка элементов экрана Профиль")
    @pytest.mark.smoke
    @pytest.mark.profile
    def test_profile_elements(self, authorization):
        self.menu.open_profile()
        self.profile.checking_profile_elements()

    @allure.title("Проверка отдельных элементов экрана Профиль")
    @pytest.mark.smoke
    @pytest.mark.profile
    def test_profile_other_elements(self, authorization):
        self.menu.open_profile()
        self.profile.checking_profile_other_elements()
