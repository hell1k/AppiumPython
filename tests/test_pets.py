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












        





