from pages.base_page import BasePage
from pages.business_page import BusinessPage
from pages.groups_page import GroupsPage
from pages.channels_page import ChannelsPage
from pages.jobs_page import JobsPage
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
    business = BusinessPage()
    jobs = JobsPage()



