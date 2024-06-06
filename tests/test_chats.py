import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Chats")
class TestChats:
    @allure.title("Проверка добавления и удаления стикер пака новым пользователем")
    @pytest.mark.smoke
    @pytest.mark.chats
    def test_add_and_del_sticker_pack(self):
        page = MainPage()
        page.login.registration()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        new_message = faker.text()
        page.channels.send_message(new_message)
        page.chats.checking_comment()
        page.chats.add_sticker_pack_comment()
        page.chats.check_send_sticker()
        page.chats.del_sticker_pack()

    @allure.title("Проверка открытия разделов на экране Chats")
    @pytest.mark.smoke
    @pytest.mark.chats
    def test_add_and_del_sticker_pack(self):
        page = MainPage()
        page.login.registration()
        page.menu.open_chats()
        page.chats.checking_clear_chat()

    @allure.title("Проверка разделов Chats")
    @pytest.mark.smoke
    @pytest.mark.chats
    def test_add_and_del_sticker_pack(self, authorization):
        page = MainPage()
        page.menu.open_chats()
        page.chats.open_events_tab()

        print('test')









