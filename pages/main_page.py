from pages.base_page import BasePage
from pages.groups_page import GroupsPage
from pages.channels_page import ChannelsPage
from pages.login_page import LoginPage
from common.menu import Menu
from pages.profile_page import ProfilePage
from pages.events_page import EventsPage


class MainPage(BasePage):
    login = LoginPage()
    menu = Menu()
    profile = ProfilePage()
    groups = GroupsPage()
    channels = ChannelsPage()
    events = EventsPage()



