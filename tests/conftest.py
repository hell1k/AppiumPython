import pytest
import uiautomator2 as u

from pages.login_page import LoginPage
from pages.menu import Menu
from pages.profile_page import ProfilePage

d = u.connect("emulator-5554")


def open_app():
    d.implicitly_wait(10)
    d.app_install("/home/el_erizo/Загрузки/AppiumPython/yapmap.apk")
    # d.uiautomator.stop()
    # d.uiautomator.start()
    d.press('home')
    d.app_clear("com.yapmap.yapmap")
    d.app_start("com.yapmap.yapmap")


def teardown():
    # d.app_clear("com.yapmap.yapmap")
    d.app_stop("com.yapmap.yapmap")


@pytest.fixture()
def setup(request):
    request.cls.login = LoginPage()
    request.cls.menu = Menu()
    request.cls.profile = ProfilePage()
    open_app()
    yield
    teardown()

