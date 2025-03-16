import allure

from pages.base_page import BasePage


class Permission(BasePage):
    permission_allow = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    photo_permission_allow = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
    while_using_the_app = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]'
    permission_allow_all_button = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_all_button"]'

    @allure.step("Permission. While using the app")
    def click_while_using_the_app(self):
        try:
            self.click(self.while_using_the_app)
        except:
            pass

    @allure.step("Permission. Close permission")
    def click_allow(self):
        self.wait_a_second()
        try:
            self.click(self.permission_allow)
        except:
            pass

    @allure.step("Permission. Permission allow")
    def close_photo_permission(self):
        self.wait_a_second()
        try:
            self.click(self.photo_permission_allow)
        except:
            pass
        self.wait_a_second()

    @allure.step("Permission. Permission allow all button")
    def close_allow_all_button(self):
        self.wait_a_second()
        try:
            self.click(self.permission_allow_all_button)
        except:
            pass
        self.wait_a_second()