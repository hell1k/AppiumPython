import random

from faker import Faker

from pages.base_page import BasePage
from pages.menu import Menu

faker = Faker()


class ProfilePage(BasePage):
    menu = Menu()

    edit_profile_icon = "com.yapmap.yapmap:id/edit_view"
    first_name_field = '//*[@resource-id="com.yapmap.yapmap:id/first_name_field"]'
    last_name_field = '//*[@resource-id="com.yapmap.yapmap:id/last_name_field"]'
    nickname_field = '//*[@resource-id="com.yapmap.yapmap:id/nickname_field"]'
    save_btn = "com.yapmap.yapmap:id/action_show_option_menu"
    first_name_view = "com.yapmap.yapmap:id/first_name_text_view"
    last_name_view = "com.yapmap.yapmap:id/last_name_text_view"
    nickname_view = "com.yapmap.yapmap:id/nickname_text_view"

    def edit_profile(self):
        self.click(self.edit_profile_icon)
        new_first_name = faker.first_name()
        new_last_name = faker.last_name()
        new_nickname = "nickname" + str(random.randint(0, 99999))
        self.set_text(self.first_name_field, new_first_name)
        self.set_text(self.last_name_field, new_last_name)
        self.set_text(self.nickname_field, new_nickname)
        self.click(self.save_btn)
        assert self.get_text(self.first_name_view) == new_first_name
        assert self.get_text(self.last_name_view) == new_last_name
        assert self.get_text(self.nickname_view) == '@' + new_nickname

