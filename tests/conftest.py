import time

import allure
import pytest
import uiautomator2 as u

from pages.groups_page import GroupsPage
from pages.login_page import LoginPage
from common.menu import Menu
from common.permission import Permission
from pages.profile_page import ProfilePage
from common.welcome_page import WelcomeActivity

d = u.connect("emulator-5554")


@allure.step("Запуск приложения")
def open_app():
    d.implicitly_wait(10)
    # d.app_install("/home/qasquad/Загрузки/yapmap.apk")
    # d.uiautomator.stop()
    # d.uiautomator.start()
    d.press('home')
    d.app_clear("com.yapmap.yapmap")
    d.app_start("com.yapmap.yapmap")


@allure.step("Закрытие приложения")
def teardown():
    # d.app_clear("com.yapmap.yapmap")
    d.app_stop("com.yapmap.yapmap")


@pytest.fixture()
def setup(request):
    request.cls.login = LoginPage()
    request.cls.menu = Menu()
    request.cls.profile = ProfilePage()
    request.cls.groups = GroupsPage()
    open_app()
    WelcomeActivity().close_tutorial()
    yield
    teardown()


@pytest.fixture()
def authorization():
    LoginPage().authorization()
    Permission().click_allow()


@pytest.fixture()
def install_app():
    d.press('home')
    time.sleep(1)
    d.app_install("http://http://37.195.111.39/:8080/job/Test/ws/yapmap.apk")
