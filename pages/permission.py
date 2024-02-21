import allure

from pages.base_page import BasePage


class Permission(BasePage):
    permission_allow = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    photo_permission_allow = '//*[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'

    @allure.step("Close permission")
    def click_allow(self):
        try:
            self.click(self.permission_allow)
        except:
            pass

    def close_photo_permission(self):
        try:
            self.click(self.photo_permission_allow)
        except:
            pass