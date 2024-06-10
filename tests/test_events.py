import time
import allure
import pytest
from config import *
from pages.main_page import MainPage


@pytest.mark.usefixtures("setup")
@allure.feature("Events")
class TestEvents:

    @allure.title("Создание нового приватного события")
    @pytest.mark.smoke
    @pytest.mark.events
    @pytest.mark.login_marker('relagram.auto+events@yandex.ru')
    def test_create_new_private_event(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event('private')
        page.events.edit_event(event_name)

    @allure.title("Создание нового не приватного события")
    @pytest.mark.smoke
    @pytest.mark.events
    @pytest.mark.login_marker('relagram.auto+events@yandex.ru')
    def test_create_new_event(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event()
        page.events.edit_event(event_name)

    @allure.title("Проверка элементов приватного события при редактировании")
    @pytest.mark.smoke
    @pytest.mark.events
    @pytest.mark.login_marker('relagram.auto+events@yandex.ru')
    def test_private_event_checking_elements(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event('private')
        page.events.open_event(event_name)
        page.events.checking_event_name_limit(event_name)
        page.events.add_to_favorite()
        page.events.checking_more_options()
        page.events.checking_more_options_private()
        page.events.edit_members()
        page.press_back()
        page.events.delete_and_leave(event_name)

    @allure.title("Проверка элементов события при редактировании")
    @pytest.mark.smoke
    @pytest.mark.events
    @pytest.mark.login_marker('relagram.auto+events@yandex.ru')
    def test_event_checking_elements(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event()
        page.events.open_event(event_name)
        page.events.checking_event_name_limit(event_name)
        page.events.add_to_favorite()
        page.events.checking_more_options()
        page.events.edit_members()
        page.press_back()
        page.events.delete_and_leave(event_name)

    @allure.title("Взаимодействие с событием участника")
    @pytest.mark.smoke
    @pytest.mark.events
    @pytest.mark.login_marker('relagram.auto+events@yandex.ru')
    def test_events_other_user(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.open_bottom_sheet()
        page.events.user_open_event(event_name)
        page.events.click_edit()
        page.events.add_to_favorite()
        page.events.checking_more_options()
        page.events.checking_more_options_join()
        page.events.checking_leave_btn(event_name)
        page.events.join_event()
        page.events.checking_report_btn()
        page.events.checking_leave_btn(event_name)

    @allure.title("Проверка отправки всех типов медиа в чат EVENTS и очистка чата")
    @pytest.mark.smoke
    @pytest.mark.events
    @pytest.mark.chats
    @pytest.mark.login_marker('relagram.auto+events@yandex.ru')
    def test_event_chat(self):
        page = MainPage()
        # page.login.authorization('relagram.auto+events@yandex.ru', 'Qq12345678!')
        page.profile.open_events()
        event_name = page.events.add_new_event()
        page.events.user_open_event(event_name)
        page.events.checking_chat_btn()
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images()
        page.chats.check_send_attachment()
        new_message = faker.text()
        page.events.send_message(new_message)
        page.chats.back_from_chat_to_main()
        page.click_back_btn()
        page.click_back_btn()

        page.menu.open_chats()
        page.chats.open_events_tab()
        page.events.open_event(event_name)
        page.chats.check_message_in_chat(new_message)

        page.events.click_edit()
        page.swipe_to_element(page.events.clear_chat_history_btn)
        page.events.clear_chat_history()
        page.events.checking_empty_chat()

        page.chats.back_from_chat_to_main()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.events.user_open_event(event_name)
        page.events.checking_empty_chat()


