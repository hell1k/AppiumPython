import allure

from pages.base_page import BasePage


class Menu(BasePage):
    profile_icon = '//*[@text="Profile"]'

    @allure.step("Переход в профиль")
    def open_profile(self):
        self.click(self.profile_icon, "иконка профиля")

