import allure
import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Business")
class TestBusiness:
    @allure.title("Создание, редактирование, удаление")
    @pytest.mark.smoke
    def test_create_new_business(self, authorization):
        page = MainPage()
        page.profile.open_business()
        business_name = page.business.add_new_business()
        page.wait_text(business_name)
        new_business_name = page.business.edit_business(business_name)
        page.business.delete_business(new_business_name)
