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
        page.menu.open_groups()
        group_name = page.groups.add_new_group()
        page.groups.open_an_open_group(group_name)
        page.chats.check_send_emoji()
        page.chats.check_send_sticker()
        page.chats.check_send_images()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_attachment()
