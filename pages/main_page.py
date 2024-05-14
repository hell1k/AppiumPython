import allure

from pages.base_page import BasePage
from pages.business_page import BusinessPage
from pages.groups_page import GroupsPage
from pages.channels_page import ChannelsPage
from pages.login_page import LoginPage
from common.menu import Menu
from pages.profile_page import ProfilePage
from pages.events_page import EventsPage
from pages.pets_page import PetsPage
from pages.chats_page import ChatsPage


class MainPage(BasePage):
    login = LoginPage()
    menu = Menu()
    profile = ProfilePage()
    groups = GroupsPage()
    channels = ChannelsPage()
    events = EventsPage()
    business = BusinessPage()
    pets = PetsPage()
    chats = ChatsPage()

    pets_filter = "com.yapmap.yapmap:id/pets_filter_text_view"
    shevron = '//*[@resource-id="com.yapmap.yapmap:id/dragging_view"]/android.view.View[1]'
    horizontal_scroll_filters = '//android.widget.HorizontalScrollView'
    dating_filter = "com.yapmap.yapmap:id/dating_filter_text_view"

    @allure.step("Открываем свайпом боттом шит")
    def open_bottom_sheet(self):
        center = self.get_element(self.shevron).center()
        fx, fy = center
        ty = self.d.window_size()[1]*0.1
        tx = self.d.window_size()[0]/2
        self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)

    @allure.step("Выбрать фильтр Pets")
    def select_pets_filter(self):
        self.swipe_horizontal_to_element(self.pets_filter)
        self.click(self.pets_filter)

    def swipe_horizontal_filters(self):
        fx, fy = self.get_element(self.horizontal_scroll_filters).center()
        tx, ty = self.get_element(self.dating_filter).center()
        self.swipe_coordinate(fx, fy, tx, ty)

    def swipe_horizontal_to_element(self, locator):
        for i in range(3):
            if self.get_elements_amount(locator) == 0:
                self.swipe_horizontal_filters()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break




