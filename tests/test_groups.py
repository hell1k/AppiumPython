import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Группы")
class TestGroups:

    @allure.title("Создание новой приватной группы")
    @pytest.mark.smoke
    @pytest.mark.groups
    def test_create_new_private_group(self, authorization):
        self.menu.open_groups()
        group_name = self.groups.add_new_group('private')
        self.groups.edit_group(group_name)

    @allure.title("Создание новой не приватной группы")
    @pytest.mark.smoke
    @pytest.mark.groups
    def test_create_new_group(self, authorization):
        self.menu.open_groups()
        group_name = self.groups.add_new_group()
        self.groups.edit_group(group_name)

    @allure.title("Проверка элементов группы при редактировании")
    @pytest.mark.smoke
    @pytest.mark.groups
    def test_checking_group_elements(self, authorization):
        self.menu.open_groups()
        group_name = self.groups.add_new_group()
        self.groups.open_an_open_group(group_name)
        self.groups.click_edit_group()
        self.groups.checking_group_name_limit(group_name)
        self.groups.add_to_favorite()
        self.groups.checking_more_options()
        self.groups.checking_chat_btn()
        self.groups.click_edit_group()
        self.groups.swipe_up(3)
        self.groups.checking_invite_people_btn()
        self.groups.press_back()
        self.groups.swipe_up()
        self.groups.checking_members_on_map(group_name)
        self.groups.press_back()
        self.groups.checking_blocked_members()

    @allure.title("Проверка пользовательских элементов группы")
    @pytest.mark.smoke
    @pytest.mark.groups
    def test_checking_user_items(self, authorization):
        page = MainPage()
        page.menu.open_groups()
        group_name = page.groups.add_new_group()
        page.groups.open_an_open_group(group_name)
        page.groups.click_edit_group()
        page.groups.add_admin()
        page.groups.press_back()
        page.groups.edit_members()
        page.groups.press_back()
        page.groups.press_back()
        page.groups.click_yes_popup()
        page.groups.send_message(faker.text())
        page.groups.click_edit_group()
        page.groups.delete_and_leave(group_name)

    @allure.title("Взаимодействие с группой участником группы")
    @pytest.mark.smoke
    @pytest.mark.groups
    def test_group_participant(self, authorization):
        page = MainPage()
        page.menu.open_groups()
        group_name = page.groups.add_new_group()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_groups()
        page.groups.join_an_open_group(group_name)
        page.groups.checking_report_group_btn()
        page.press_back()
        page.groups.leave_group(group_name)



