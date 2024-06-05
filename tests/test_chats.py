import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Chats")
class TestChats:
    @allure.title("Проверка отправки всех типов медиа в чат")
    @pytest.mark.smoke
    @pytest.mark.chats
    def test_send_media_in_chats(self):
        page = MainPage()
        page.login.registration()
        page.menu.open_chats()
        page.chats.open_my_notes()
        page.chats.check_send_emoji()
        page.chats.check_send_sticker()
        page.chats.check_send_images()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_attachment()

    @allure.title("Проверка отправки всех типов медиа в чат Events")
    @pytest.mark.smoke
    @pytest.mark.chats
    def test_send_media_in_chats_events(self, authorization):
        page = MainPage()
        page.menu.open_chats()
        page.chats.open_places_tab()
