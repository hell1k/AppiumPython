import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Jobs")
class TestJobs:
    @allure.title("Создание, редактирование и удаление сущности Jobs")
    @pytest.mark.smoke
    def test_create_new_jobs(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.check_business_item_availability()
        page.business.click_back_btn()
        page.profile.click_jobs()
        position_name = page.jobs.create_new_jobs()
        new_position_name = page.jobs.edit_job(position_name)
        page.jobs.delete_job(new_position_name)

    @allure.title("Взаимодействие пользователя с Jobs")
    @pytest.mark.smoke
    def test_user_jobs(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.check_business_item_availability()
        page.business.click_back_btn()
        page.profile.click_jobs()
        position_name = page.jobs.create_new_jobs()

        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.select_jobs_filter()
        page.jobs.user_open_job(position_name)
        page.jobs.add_to_favorite()
        page.jobs.checking_more_options_user()
        page.jobs.click_contact_employer()
        message = page.jobs.test_chat()
        page.login.logout()

        page.login.authorization()
        page.profile.click_jobs()


        page.jobs.delete_job(position_name)


