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
    def test_add_new_pet(self, login):
        page = MainPage()
        page.profile.open_pets()
        page.pets.add_new_pet()

