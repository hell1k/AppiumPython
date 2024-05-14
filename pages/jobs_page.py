import random

import allure
import faker
from faker import Faker

from common.menu import Menu
from common.permission import Permission
from pages.base_page import BasePage
from tests.config import text_250


class JobsPage(BasePage):
    menu = Menu()
    faker = Faker()

    hire_now_btn = 'com.yapmap.yapmap:id/create_button'
    add_new_jobs_btn = 'com.yapmap.yapmap:id/action_create'
    business_profile_required_alert = '//*[@resource-id="com.yapmap.yapmap:id/title_text_view" and @text="Business profile required"]'
    business_name = 'com.yapmap.yapmap:id/name_text_view'
    position_name_field = '//*[@resource-id="com.yapmap.yapmap:id/position_name_edit_text"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_input_layout"]'
    position_name_value = '//*[@resource-id="com.yapmap.yapmap:id/position_name_edit_text"]//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"]'
    profession_type_btn = '//*[@resource-id="com.yapmap.yapmap:id/profession_type_input_field"]//*[@resource-id="com.yapmap.yapmap:id/click_view"]'
    profession_type_list = 'com.yapmap.yapmap:id/value_text_view'
    duties_description = 'com.yapmap.yapmap:id/duties_description_edit_text'
    skills_field = 'com.yapmap.yapmap:id/skills_edit_text'
    add_photo_btn = 'com.yapmap.yapmap:id/photos_field_add_photo_text_view'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/avatar_layout"]/android.widget.FrameLayout[1]'
    job_type = '//*[@resource-id="com.yapmap.yapmap:id/job_type_input_field"]//*[@resource-id="com.yapmap.yapmap:id/click_view"]'
    values_list = 'com.yapmap.yapmap:id/value_text_view'
    apply_btn = 'com.yapmap.yapmap:id/action_apply'
    hours_per_week = '//*[@resource-id="com.yapmap.yapmap:id/hours_per_week_input_field"]//*[@resource-id="com.yapmap.yapmap:id/click_view"]'
    salary_per = '//*[@resource-id="com.yapmap.yapmap:id/salary_per_input_field"]//*[@resource-id="com.yapmap.yapmap:id/click_view"]'
    salary_amount = '//*[@resource-id="com.yapmap.yapmap:id/salary_input_field"]//*[@resource-id="com.yapmap.yapmap:id/click_view"]'
    salary_amount_field = '//*[@resource-id="com.yapmap.yapmap:id/edit_text_view" and @text="Salary amount"]'
    salary_amount_done = 'com.yapmap.yapmap:id/done_button'
    currency = '//*[@resource-id="com.yapmap.yapmap:id/currency_input_field"]//*[@resource-id="com.yapmap.yapmap:id/click_view"]'
    commission_switch = '//*[@resource-id="com.yapmap.yapmap:id/commission_switch_field"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    remotely_switch = '//*[@resource-id="com.yapmap.yapmap:id/remotely_switch_field"]//*[@resource-id="com.yapmap.yapmap:id/container"]'
    post_btn = 'com.yapmap.yapmap:id/post_button'

    @allure.step("Клик по кнопке создания новой Jobs")
    def click_create_new_jobs(self):
        self.click(self.add_new_jobs_btn, "кнопка создания новой Jobs")

    @allure.step("Создание новой Jobs")
    def create_new_jobs(self):
        self.click_create_new_jobs()
        self.wait_text("Select business")
        self.click(self.business_name, "выбор Business")
        self.wait_text("Add a new Job")
        self.set_position_name()
        position_name = self.get_text(self.position_name_value)
        self.select_profession_type()
        self.set_duties_description()
        self.swipe_up()
        self.set_skills()
        self.swipe_up(2)
        self.upload_new_photo()
        self.swipe_up()
        self.select_job_type()
        self.select_hours_per_week()
        self.select_salary_per()
        self.select_salary_amount()
        self.select_currency()
        self.click_commission_switch()
        self.wait_a_second()
        self.click_remotely_switch()
        self.swipe_to_element(self.post_btn)
        self.click_post_btn()
        self.wait_text("Your job has been accepted")
        self.wait_text(position_name)

    @allure.step("Заполнение поля Position name")
    def set_position_name(self):
        self.set_text(self.position_name_field, self.faker.job(), "Position name")

    @allure.step("Клик по кнопке Post")
    def click_post_btn(self):
        self.click(self.post_btn, "кнопка Post")

    @allure.step("Заполнение поля Duties description")
    def set_duties_description(self):
        self.set_text(self.duties_description, text_250, "Duties description")

    @allure.step("Заполнение поля Skills")
    def set_skills(self):
        self.set_text(self.skills_field, text_250, "Skills")

    @allure.step("Клик чекбокс Commission")
    def click_commission_switch(self):
        self.click(self.commission_switch, "чекбокс Commission")

    @allure.step("Клик чекбокс Can work remotely")
    def click_remotely_switch(self):
        self.click(self.remotely_switch, "чекбокс Can work remotely")

    @allure.step("Выбор profession type")
    def select_profession_type(self):
        self.click(self.profession_type_btn, 'поле Profession type')
        self.wait_element(self.profession_type_list)
        self.click(self.get_random_element(self.profession_type_list), "рандомный Professional type")

    @allure.step("Добавление нового фото")
    def upload_new_photo(self):
        self.click(self.add_photo_btn, 'add photo')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")

    @allure.step("Выбор Job type")
    def select_job_type(self):
        self.click(self.job_type, "поле Job type")
        self.wait_element(self.values_list)
        self.click(self.get_random_element(self.values_list), "рандомный Job type")
        self.click(self.apply_btn, "кнопка Apply")

    @allure.step("Выбор Hours per week")
    def select_hours_per_week(self):
        self.click(self.hours_per_week, "поле Hours per week")
        self.wait_element(self.values_list)
        self.click(self.get_random_element(self.values_list), "рандомный Hours per week")

    @allure.step("Выбор Salary per")
    def select_salary_per(self):
        self.click(self.salary_per, "поле Salary per")
        self.wait_element(self.values_list)
        self.click(self.get_random_element(self.values_list), "рандомный Salary per")

    @allure.step("Выбор Salary amount")
    def select_salary_amount(self):
        self.click(self.salary_amount, "поле Salary amount")
        self.set_text(self.salary_amount_field, str(random.randint(1000, 10000)), "Salary amount")
        self.click(self.salary_amount_done, "кнопка Done")

    @allure.step("Выбор Currency")
    def select_currency(self):
        self.click(self.currency, "поле Currency")
        self.wait_element(self.values_list)
        self.click(self.get_random_element(self.values_list), "рандомный Currency")