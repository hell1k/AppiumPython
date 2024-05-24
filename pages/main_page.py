import allure

from pages.base_page import BasePage
from pages.business_page import BusinessPage
from pages.groups_page import GroupsPage
from pages.channels_page import ChannelsPage
from pages.jobs_page import JobsPage
from pages.login_page import LoginPage
from common.menu import Menu
from pages.profile_page import ProfilePage
from pages.events_page import EventsPage
from pages.pets_page import PetsPage
from pages.chats_page import ChatsPage
from pages.market_page import MarketPage
from pages.places_page import PlacesPage


class MainPage(BasePage):
    login = LoginPage()
    menu = Menu()
    profile = ProfilePage()
    groups = GroupsPage()
    channels = ChannelsPage()
    events = EventsPage()
    business = BusinessPage()
    pets = PetsPage()
    jobs = JobsPage()
    chats = ChatsPage()
    market = MarketPage()
    place = PlacesPage()

    pets_filter = "com.yapmap.yapmap:id/pets_filter_text_view"
    shevron = '//*[@resource-id="com.yapmap.yapmap:id/dragging_view"]/android.view.View[1]'
    horizontal_scroll_filters = '//android.widget.HorizontalScrollView'
    dating_filter = "com.yapmap.yapmap:id/dating_filter_text_view"
    local_deals_filter = "com.yapmap.yapmap:id/local_deals_filter_text_view"
    jobs_filter = "com.yapmap.yapmap:id/jobs_filter_text_view"
    market_filter = "com.yapmap.yapmap:id/advertisements_filter_text_view"
    places_filter = "com.yapmap.yapmap:id/places_filter_text_view"

    @allure.step("Открываем свайпом боттом шит")
    def open_bottom_sheet(self):
        center = self.get_element(self.shevron).center()
        fx, fy = center
        ty = self.d.window_size()[1]*0.1
        tx = self.d.window_size()[0]/2
        self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)

    @allure.step("Выбрать фильтр Pets")
    def select_pets_filter(self):
        self.wait_text('Search')
        self.swipe_horizontal_to_element(self.pets_filter)
        self.click(self.pets_filter)

    @allure.step("Выбрать фильтр Local deals")
    def select_local_deals_filter(self):
        self.wait_text('Search')
        self.swipe_horizontal_to_element(self.local_deals_filter)
        self.click(self.local_deals_filter)

    @allure.step("Выбрать фильтр Jobs")
    def select_jobs_filter(self):
        self.wait_text('Search')
        self.swipe_horizontal_to_element(self.jobs_filter)
        self.click(self.jobs_filter)

    @allure.step("Выбрать фильтр Market")
    def select_market_filter(self):
        self.wait_text('Search')
        self.swipe_horizontal_to_element(self.market_filter)
        self.click(self.market_filter)

    @allure.step("Выбрать фильтр Places")
    def select_places_filter(self):
        self.wait_text('Search')
        self.swipe_horizontal_to_element(self.places_filter)
        self.click(self.places_filter)

    def swipe_horizontal_filters(self):
        fx, fy = self.get_element(self.horizontal_scroll_filters).center()
        tx, ty = self.get_element(self.dating_filter).center()
        self.swipe_coordinate(fx, fy, tx, ty)

    def swipe_horizontal_markets(self):
        x, fy = self.get_element("com.yapmap.yapmap:id/recycler_view").center()
        ty = fy
        fx = self.d.window_size()[0] - 50
        tx = 50
        self.swipe_coordinate(fx, fy, tx, ty)

    def swipe_horizontal_to_element_in_market(self, locator):
        for i in range(10):
            if self.get_elements_amount(locator) == 0:
                self.swipe_horizontal_markets()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break

    @allure.step("Открыть Market пользователем")
    def user_open_ad(self, ad_name):
        element = f'//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout//*[@text="{ad_name}"]'
        self.swipe_horizontal_to_element_in_market(element)
        self.click(element)

    def swipe_horizontal_to_element(self, locator):
        for i in range(3):
            if self.get_elements_amount(locator) == 0:
                self.swipe_horizontal_filters()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break




