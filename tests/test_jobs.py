import allure
import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Jobs")
class TestJobs:
    @allure.title("Создание сущности Jobs")
    @pytest.mark.smoke
    def test_create_new_jobs(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.check_business_item_availability()
        page.business.click_back_btn()
        page.profile.click_jobs()
        position_name = page.jobs.create_new_jobs()
        page.jobs.delete_job(position_name)


