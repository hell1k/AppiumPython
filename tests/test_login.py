import allure
import pytest
import uiautomator2 as u

from pages.permission import Permission
from pages.profile_page import ProfilePage
from pages.welcome_page import WelcomeActivity

d = u.connect("emulator-5554")


@pytest.mark.usefixtures("setup")
class TestExample:

    @allure.title("test1")
    @pytest.mark.smoke
    def test_edit_profile(self):
        self.get_screen()
        WelcomeActivity().close_tutorial()
        self.login.authorization()
        Permission().click_allow()
        self.menu.open_profile()
        self.profile.edit_profile_fields()

    @allure.title("test2")
    @pytest.mark.smoke
    def test_example2(self):
        # d = u.connect("49e9905f")
        d.app_start("com.yapmap.yapmap")
        try:
            d(resourceId="com.yapmap.yapmap:id/activity_welcome_button").click()
        except:
            pass
        self.get_screen()
        d(resourceId="com.yapmap.yapmap:id/sign_up_button").click()
        d.xpath(
            '//*[@resource-id="com.yapmap.yapmap:id/email_edit_text_layout"]/android.widget.FrameLayout[1]').set_text(
            "test@test.ru")
        d.xpath(
            '//*[@resource-id="com.yapmap.yapmap:id/invite_code_edit_text_layout"]/android.widget.FrameLayout[1]').set_text(
            "123456")
        d.xpath(
            '//*[@resource-id="com.yapmap.yapmap:id/password_edit_text_layout"]/android.widget.FrameLayout[1]').set_text(
            "123456")

        self.get_screen()
        d.xpath(
            '//*[@resource-id="com.yapmap.yapmap:id/confirm_password_edit_text_layout"]/android.widget.FrameLayout[1]').set_text(
            "1234567")
        d(resourceId="com.yapmap.yapmap:id/sign_up_button").click()
        self.get_screen()
        d.app_clear("com.yapmap.yapmap")
        d.app_stop("com.yapmap.yapmap")

    @allure.description("Проверка редактирования полей профиля")
    def test_test(self):
        WelcomeActivity().close_tutorial()
        self.login.authorization()
        Permission().click_allow()
        self.menu.open_profile()
        self.profile.click_edit_profile()
        profile_data = self.profile.edit_profile()
        self.profile.click_edit_profile()
        self.profile.check_data_name(profile_data[0])
        self.profile.check_data_name(profile_data[1])
        self.profile.check_data_name(profile_data[2])
        self.profile.check_data_name(profile_data[3])
        self.profile.check_data_name(profile_data[4])

    @allure.description("Проверка отмены редактирования")
    def test_checking_undoing_changes(self):
        WelcomeActivity().close_tutorial()
        self.login.authorization()
        Permission().click_allow()
        self.menu.open_profile()
        self.profile.canceling_changes()



def test_t1():
    page = ProfilePage()
    print(page.d.window_size()[1])
