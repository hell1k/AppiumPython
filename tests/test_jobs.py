import time

import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Jobs")
class TestJobs:
    @allure.title("Создание, редактирование и удаление сущности Jobs")
    @pytest.mark.smoke
    @pytest.mark.jobs
    def test_create_new_jobs(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.check_business_item_availability()
        page.business.click_back_btn()
        page.profile.click_jobs()
        position_name = page.jobs.create_new_jobs()
        page.jobs.open_create_job(position_name)
        page.jobs.add_to_favorite()
        page.jobs.checking_more_options()
        new_position_name = page.jobs.edit_job(position_name)
        page.jobs.delete_job(new_position_name)




