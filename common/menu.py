import allure

from pages.base_page import BasePage


class Menu(BasePage):
    profile_icon = '//*[@text="Profile"]'
    groups_icon = '//*[@resource-id="com.yapmap.yapmap:id/groups_button"]'
    channels_icon = '//*[@resource-id="com.yapmap.yapmap:id/channels_button"]'

    @allure.step("Переход в профиль")
    def open_profile(self):
        self.click(self.profile_icon, "Profile")

    @allure.step("Переход в раздел Groups")
    def open_groups(self):
        self.click(self.groups_icon, 'Groups')

    @allure.step("Переход в раздел Channels")
    def open_channels(self):
        self.click(self.channels_icon, 'Channels')
