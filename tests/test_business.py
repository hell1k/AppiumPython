import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Business")
class TestBusiness:
    @allure.title("Создание, редактирование, удаление")
    @pytest.mark.smoke
    @pytest.mark.business
    def test_business_lifecycle(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.clear_business()
        business_name = page.business.add_new_business()
        page.wait_text(business_name)
        new_business_name = page.business.edit_business(business_name)
        page.business.delete_business(new_business_name)

    @allure.title("Проверка полей сущности Business")
    @pytest.mark.smoke
    @pytest.mark.business
    def test_checking_edit_business(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.clear_business()
        page.business.add_new_business_with_full_fields()
        assert page.get_text(page.business.business_item) in text_250_2
        assert page.get_text(page.business.description_in_business_list) in text_250
        page.business.delete_business(page.get_text(page.business.business_item))
        page.business.checking_empty_business_page()



