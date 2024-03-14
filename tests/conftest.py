import allure
import pytest
import uiautomator2 as u

from pages.login_page import LoginPage
from pages.menu import Menu
from pages.permission import Permission
from pages.profile_page import ProfilePage
from pages.welcome_page import WelcomeActivity

d = u.connect("emulator-5554")


@allure.step("Запуск приложения")
def open_app():
    d.implicitly_wait(10)
    d.app_install("/home/qasquad/Загрузки/yapmap.apk")
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
    d.app_install("/home/qasquad/Загрузки/yapmap.apk")
