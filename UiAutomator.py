import time

import allure
import pytest
import uiautomator2 as u


# python3 -m pytest UiAutomator.py::test_example

class TestExample:
    @allure.title("test1")
    @pytest.mark.smoke
    def test_example(self):
        d = u.connect("emulator-5554")
        # d = u.connect("49e9905f")
        d.app_start("com.yapmap.yapmap")
        try:
            d(resourceId="com.yapmap.yapmap:id/activity_welcome_button").click()
        except:
            pass
        d(resourceId="com.yapmap.yapmap:id/sign_in_button").click()
        d.xpath(
            '//*[@resource-id="com.yapmap.yapmap:id/email_edit_text_layout"]/android.widget.FrameLayout[1]').set_text(
            "test@test.ru")
        d.xpath(
            '//*[@resource-id="com.yapmap.yapmap:id/password_edit_text_layout"]/android.widget.FrameLayout[1]').set_text(
            "12345678")
        d(resourceId="com.yapmap.yapmap:id/sign_in_button").click()
        d.app_clear("com.yapmap.yapmap")
        d.app_stop("com.yapmap.yapmap")

    @allure.title("test2")
    @pytest.mark.smoke
    def test_example2(self):
        d = u.connect("emulator-5554")
        # d = u.connect("49e9905f")
        d.app_start("com.yapmap.yapmap")
        try:
            d(resourceId="com.yapmap.yapmap:id/activity_welcome_button").click()
        except:
            pass
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
        d.xpath(
            '//*[@resource-id="com.yapmap.yapmap:id/confirm_password_edit_text_layout"]/android.widget.FrameLayout[1]').set_text(
            "1234567")
        d(resourceId="com.yapmap.yapmap:id/sign_up_button").click()
        d.app_clear("com.yapmap.yapmap")
        d.app_stop("com.yapmap.yapmap")
