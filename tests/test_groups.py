import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
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

    @allure.step("Проверка элементов группы при редактировании")
    @pytest.mark.groups
    def test_checking_group_elements(self, authorization):
        self.menu.open_groups()
        group_name = self.groups.open_or_create_group()
        self.groups.click_edit_group()
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

    @allure.step("Проверка пользовательских элементов группы")
    @pytest.mark.groups
    def test_checking_user_items(self, authorization):
        self.menu.open_groups()
        group_name = self.groups.open_or_create_group()
        self.groups.click_edit_group()
        self.groups.swipe_up(5)
        self.groups.add_admin()
        self.groups.press_back()
        self.groups.edit_members()
        self.groups.press_back()
        self.groups.press_back()
        self.groups.send_message(faker.text())
        self.groups.click_edit_group()
        self.groups.swipe_up(5)
        self.groups.delete_and_leave(group_name)

    @allure.step("Взаимодействие с группой участником группы")
    @pytest.mark.groups
    def test_group_participant(self, authorization):
        page = MainPage()
        page.menu.open_groups()
        group_name = page.groups.open_or_create_group()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_groups()
        page.groups.join_a_group(group_name)
        page.swipe_up(3)
        page.groups.checking_report_group_btn()
        page.press_back()
        page.groups.leave_group(group_name)

    @allure.step("Очистка чата администратором")
    @pytest.mark.groups
    def test_clear_chat(self, authorization):
        page = MainPage()
        page.menu.open_groups()
        group_name = page.groups.open_or_create_group()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_groups()
        page.groups.join_a_group(group_name)
        page.groups.click_chat_icon()
        new_message = faker.text()
        page.groups.send_message(new_message)
        page.press_back()
        page.press_back()
        page.login.logout()
        page.login.authorization()
        page.menu.open_groups()
        page.groups.open_group(group_name)
        page.groups.click_edit_group()
        page.swipe_up(5)
        page.groups.clear_chat_history()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_groups()
        page.groups.open_group(group_name)
        page.groups.checking_empty_chat()

