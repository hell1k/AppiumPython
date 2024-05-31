import random

import allure
import faker
from faker import Faker
from common.menu import Menu
from common.permission import Permission
from pages.base_page import BasePage
from tests.config import *


class FavoritesPage(BasePage):
    menu = Menu()
    faker = Faker()

    edit_btn = "com.yapmap.yapmap:id/action_edit"
    cancel_button = "com.yapmap.yapmap:id/cancel_button"
    delete_button = "com.yapmap.yapmap:id/delete_button"

    def open_item(self, name):
        self.swipe_to_element(self.d(f'//*[@text="{name}"]/..'))
        self.click(self.d(f'//*[@text="{name}"]/..'))

    def check_name(self, name):
        self.wait_a_second()
        self.wait_text(name)

    def click_edit(self):
        self.click(self.edit_btn, 'кнопка Редактировать (карандаш в верхнем правом углу)')
        self.wait_a_moment()
