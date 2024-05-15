import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Pets")
class TestPets:

    @allure.title("Добавление нового питомца")
    @pytest.mark.smoke
    @pytest.mark.pets
    # @pytest.mark.login_marker("relagram.auto+pets@yandex.ru")
    def test_add_new_pet(self, authorization):
        page = MainPage()
        page.profile.open_pets()
        page.pets.add_new_pet_btn()
        page.pets.click_ok()
        page.pets.add_photo()
        pet_name = page.pets.add_new_pet()
        page.pets.check_pet_in_list(pet_name)

    @allure.title("Редактирование питомца")
    @pytest.mark.smoke
    @pytest.mark.pets
    # @pytest.mark.login_marker("relagram.auto+pets@yandex.ru")
    def test_edit_pet(self, authorization):
        page = MainPage()
        page.profile.open_pets()
        page.pets.add_new_pet_btn()
        page.pets.click_ok()
        page.pets.add_photo()
        pet_name = page.pets.add_new_pet()
        page.pets.check_pet_in_list(pet_name)
        page.pets.open_pet(pet_name)
        page.pets.checking_more_options()
        page.pets.add_to_favorite()
        new_pet_name = page.pets.edit_pet()
        page.pets.open_pet(new_pet_name)
        page.pets.delete_pet(new_pet_name)

    @allure.title("Взаимодействие другого пользователя с питомцем")
    @pytest.mark.smoke
    @pytest.mark.pets
    # @pytest.mark.login_marker("relagram.auto+pets@yandex.ru")
    def test_user_pet(self, authorization):
        # Создаем питомца пользователем 1
        page = MainPage()
        page.profile.open_pets()
        page.pets.add_new_pet_btn()
        page.pets.click_ok()
        page.pets.add_photo()
        pet_name = page.pets.add_new_pet()
        page.press_back()
        page.pets.check_pet_in_list(pet_name)
        page.pets.click_back_btn()
        page.login.logout()
        # Создаем питомца пользователем 2
        page.login.authorization(test_user_login, test_user_password)
        page.select_pets_filter()
        page.pets.user_dont_have_pets_msg_check()
        page.pets.click_cancel()
        page.select_pets_filter()
        page.pets.user_dont_have_pets_msg_check()
        page.pets.click_ok()
        page.pets.pets_check_msg()
        page.pets.click_ok()
        page.pets.add_photo_without_permissions()
        user_pet_name = page.pets.add_new_pet()
        # Открываем пользователем 2 питомца пользователя 1
        page.select_pets_filter()
        page.open_bottom_sheet()
        page.pets.open_pet(pet_name)
        page.pets.checking_more_options_user()
        page.pets.add_to_favorite()
        # Отправляем сообщение питомцу 1 от питомца 2
        page.pets.click_send_message()
        page.pets.open_pet(user_pet_name)
        message = page.pets.test_chat()
        page.login.logout()
        # Проверяем что пользователь 1 увидит сообщение пользователя 2
        page.login.authorization()
        # Путь проверки - 'Профиль - Чат - Pets - I own - name_pet - user_pet_name'
        page.menu.open_chats()
        page.chats.check_pets_message(pet_name, user_pet_name, message)
        # Путь проверки - 'Фильтр - name_pet - user_pet_name'
        # page.select_pets_filter()
        # page.open_bottom_sheet()
        # page.pets.open_pet(pet_name)









        





