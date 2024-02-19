from pages.base_page import BasePage


class Permission(BasePage):
    permission_allow = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"

    def click_allow(self):
        try:
            self.click(self.permission_allow)
        except:
            pass