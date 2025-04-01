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
from pages.favorites_page import FavoritesPage
from pages.ticker_page import TickerPage


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
    favorites = FavoritesPage()
    ticker = TickerPage()

    pets_filter = "com.yapmap.yapmap:id/pets_filter_text_view"
    shevron = '//*[@resource-id="com.yapmap.yapmap:id/dragging_view"]/android.view.View[1]'
    horizontal_scroll_filters = '//android.widget.HorizontalScrollView'
    dating_filter = "com.yapmap.yapmap:id/dating_filter_text_view"
    local_deals_filter = "com.yapmap.yapmap:id/local_deals_filter_text_view"
    jobs_filter = "com.yapmap.yapmap:id/jobs_filter_text_view"
    market_filter = "com.yapmap.yapmap:id/advertisements_filter_text_view"
    places_filter = "com.yapmap.yapmap:id/places_filter_text_view"
    events_filter = "com.yapmap.yapmap:id/events_filter_text_view"
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'

    @allure.step("Нажатие кнопки 'Назад")
    def click_back_btn(self):
        self.click(self.d(description="Back"), "кнопка Назад")

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.wait_a_second()
        self.wait_a_second()
        self.click(self.add_to_favorites_btn, "кнопка добавления в избранное")
        self.wait_a_second()

    @allure.step("Подтверждение изменений")
    def unsaved_changes_popup_click_yes(self):
        if self.get_elements_amount('//*[@text="YES"]') > 0:
            self.click('//*[@text="YES"]')
            self.wait_a_second()

    @allure.step("Открываем свайпом боттом шит")
    def open_bottom_sheet(self):
        center = self.get_element(self.shevron).center()
        fx, fy = center
        ty = self.d.window_size()[1]*0.1
        tx = self.d.window_size()[0]/2
        self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)
        self.wait_a_second()

    @allure.step("Открываем свайпом боттом шит")
    def open_bottom_sheet_a_bit(self):
        center = self.get_element(self.shevron).center()
        fx, fy = center
        ty = self.d.window_size()[1] * 0.5
        tx = self.d.window_size()[0] / 2
        self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)


    @allure.step("Закрываем боттом шит свайпом вниз")
    def close_bottom_sheet(self):
        center = self.get_element(self.shevron).center()
        fx, fy = center
        ty = self.d.window_size()[1] * 0.9  # Смещаем вниз
        tx = self.d.window_size()[0] / 2
        self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)


        # start_x = self.d.window_size()[0] / 2
        # start_y = self.d.window_size()[1] * 0.2
        # end_y = self.d.window_size()[1] * 0.8
        # self.d.swipe(start_x, start_y, start_x, end_y, duration=0.2)
        # self.wait_a_moment()


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

    @allure.step("Выбрать фильтр Events")
    def select_events_filter(self):
        self.wait_text('Search')
        self.click(self.events_filter, 'Events')

    @allure.step("Выбрать фильтр Market")
    def select_market_filter(self):
        self.wait_text('Search')
        self.swipe_horizontal_to_element(self.market_filter)
        self.click(self.market_filter)

    @allure.step("Выбрать фильтр Places")
    def select_places_filter(self):
        # self.wait_text('Search')
        self.wait_a_second()
        self.swipe_horizontal_to_element(self.places_filter)
        self.wait_a_second()
        self.click(self.places_filter)
        self.wait_a_second()

    @allure.step("swipe_horizontal_filters")
    def swipe_horizontal_filters(self):
        fx, fy = self.get_element(self.horizontal_scroll_filters).center()
        tx, ty = self.get_element(self.dating_filter).center()
        self.swipe_coordinate(fx, fy, tx, ty)

    @allure.step("swipe_horizontal_markets")
    def swipe_horizontal_markets(self):
        x, fy = self.get_element("com.yapmap.yapmap:id/recycler_view").center()
        ty = fy
        fx = self.d.window_size()[0] - 50
        tx = 50
        self.swipe_coordinate(fx, fy, tx, ty)

    @allure.step("swipe_horizontal_to_element_in_market")
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
        self.wait_a_second()
        element = f'//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout//*[@text="{ad_name}"]'
        self.swipe_horizontal_to_element_in_market(element)
        self.click(element)

    @allure.step("Открыть Place пользователем")
    def user_open_place(self, place_name):
        element = f'//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout//*[@text="{place_name}"]'
        self.wait_element(element)
        self.swipe_down_to_element(element)
        self.click(element)

    @allure.step("swipe_horizontal_to_element")
    def swipe_horizontal_to_element(self, locator):
        for i in range(3):
            if self.get_elements_amount(locator) == 0:
                self.swipe_horizontal_filters()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break






