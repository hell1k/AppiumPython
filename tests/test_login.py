import allure
import pytest
import uiautomator2 as u

from pages.permission import Permission
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
        self.profile.edit_profile()
        # d.swipe(400, 1000, 400, 500)
        # assert d(resourceId="com.yapmap.yapmap:id/referral_code_button").exists() == True


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

    def get_screen(self):
        screen = "screen.png"
        d.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)


def test_test():
    u.Device()._setup_uiautomator()
    u.Device()._prepare_atx_agent()
    # d.xpath('//*[@resource-id="com.yapmap.yapmap:id/first_name_field"]').set_text("qeqwe")
