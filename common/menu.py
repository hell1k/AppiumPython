import allure

from pages.base_page import BasePage


class Menu(BasePage):
    profile_icon = '//*[@text="Profile"]'
    groups_icon = '//*[@resource-id="com.yapmap.yapmap:id/groups_button"]'
    channels_icon = '//*[@resource-id="com.yapmap.yapmap:id/channels_button"]'
    chats_icon = '//*[@resource-id="com.yapmap.yapmap:id/chat_button"]'
    search_icon = '//*[@resource-id="com.yapmap.yapmap:id/search_button"]'

    @allure.step("Переход в профиль")
    def open_profile(self):
        self.click(self.profile_icon, "Profile")

    @allure.step("Переход в раздел Groups")
    def open_groups(self):
        self.wait_a_second()
        self.click(self.groups_icon, 'Groups')
        self.wait_a_second()

    @allure.step("Переход в раздел Channels")
    def open_channels(self):
        self.click(self.channels_icon, 'Channels')

    @allure.step("Переход в раздел Chats")
    def open_chats(self):
        self.click(self.chats_icon, 'Chats')
        self.wait_text('People')

    @allure.step("Переход в раздел Search")
    def open_search(self):
        self.click_back_btn()
        self.click(self.search_icon, 'Chats')
        self.wait_text('Search')

