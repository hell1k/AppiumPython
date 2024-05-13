import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Events")
class TestPets:

    @allure.title("Добавление нового питомца")
    @pytest.mark.smoke
    @pytest.mark.pets
    # @pytest.mark.login_marker("relagram.auto+pets@yandex.ru")
    def test_add_new_pet(self, authorization):
        page = MainPage()
        page.profile.open_pets()
        page.pets.add_new_pet()

    @allure.title("Редактирование питомца")
    @pytest.mark.smoke
    @pytest.mark.pets
    # @pytest.mark.login_marker("relagram.auto+pets@yandex.ru")
    def test_edit_pet(self, authorization):
        page = MainPage()
        page.profile.open_pets()
        pet_name = page.pets.add_new_pet()
        page.pets.open_pet(pet_name)
        page.pets.checking_more_options()
        page.pets.add_to_favorite()
        new_pet_name = page.pets.edit_pet()
        page.pets.open_pet(new_pet_name)
        page.pets.delete_pet(new_pet_name)

    @allure.title("Взаимодействие другого пользователя ")
    @pytest.mark.smoke
    @pytest.mark.pets
    # @pytest.mark.login_marker("relagram.auto+pets@yandex.ru")
    def test_edit_pet(self, authorization):
        page = MainPage()
        page.profile.open_pets()
        pet_name = page.pets.add_new_pet()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.select_pets_filter()
        page.open_bottom_sheet()
        page.pets.open_pet(pet_name)
        





