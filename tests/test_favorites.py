import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Favorites")
class TestFavorites:
    @allure.title("Добавление в избранное groups")
    @pytest.mark.smoke
    @pytest.mark.favorites
    def test_add_to_favorite_groups(self, authorization):
        page = MainPage()
        page.menu.open_groups()
        group_name = page.groups.add_new_group()
        page.groups.open_an_open_group(group_name)
        page.groups.click_edit_group()
        page.add_to_favorite()
        page.favorites.favorite_btn_wait_color()
        page.groups.click_save()
        page.press_back()
        page.profile.open_favorites()
        page.favorites.open_item('Groups')
        page.favorites.check_name(group_name)

    @allure.title("Добавление в избранное event")
    @pytest.mark.smoke
    @pytest.mark.favorites
    def test_add_to_favorite_event(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event()
        page.events.open_event(event_name)
        page.add_to_favorite()
        page.favorites.favorite_btn_wait_color()
        page.click_back_btn()
        page.press_back()
        page.profile.open_favorites()
        page.favorites.open_item('Events')
        page.favorites.check_name(event_name)

    @allure.title("Добавление в избранное business")
    @pytest.mark.smoke
    @pytest.mark.favorites
    def test_add_to_favorite_business(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.clear_business()
        business_name = page.business.add_new_business()
        page.business.open_business(business_name)
        page.add_to_favorite()
        page.favorites.favorite_btn_wait_color()
        page.click_back_btn()
        page.press_back()
        page.profile.open_favorites()
        page.favorites.open_item('Local deals')
        page.favorites.check_name(business_name)

    @allure.title("Добавление в избранное market")
    @pytest.mark.smoke
    @pytest.mark.favorites
    def test_add_to_favorite_market(self, authorization):
        page = MainPage()
        page.profile.open_market()
        page.market.click_plus_new_market()
        page.market.click_create()
        ad_name = page.market.create_new_ad_stuff()
        page.market.open_market(ad_name)
        page.add_to_favorite()
        page.favorites.favorite_btn_wait_color()
        page.click_back_btn()
        page.press_back()
        page.profile.open_favorites()
        page.favorites.open_item('Market')
        page.favorites.check_name(ad_name)

    @allure.title("Добавление в избранное channel")
    @pytest.mark.smoke
    @pytest.mark.favorites
    def test_add_to_favorite_channel(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        page.channels.click_edit_channel()
        page.add_to_favorite()
        page.favorites.favorite_btn_wait_color()
        page.click_back_btn()
        page.press_back()
        page.press_back()
        page.profile.open_favorites()
        page.favorites.open_item('Channels')
        page.favorites.check_name(channel_name)

    @allure.title("Добавление в избранное jobs")
    @pytest.mark.smoke
    @pytest.mark.favorites
    def test_add_to_favorite_jobs(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.check_business_item_availability()
        page.business.click_back_btn()
        page.profile.click_jobs()
        job_name = page.jobs.create_new_jobs()
        page.add_to_favorite()
        page.favorites.favorite_btn_wait_color()
        page.click_back_btn()
        page.press_back()
        page.profile.open_favorites()
        page.favorites.open_item('Jobs')
        page.favorites.check_name(job_name)

    @allure.title("Добавление в избранное pets")
    @pytest.mark.smoke
    @pytest.mark.favorites
    def test_add_to_favorite_pets(self, authorization):
        page = MainPage()
        page.profile.open_pets()
        page.pets.add_new_pet_btn()
        page.pets.click_ok()
        page.pets.add_photo()
        pet_name = page.pets.add_new_pet()
        page.pets.open_pet(pet_name)
        page.add_to_favorite()
        page.favorites.favorite_btn_wait_color()
        page.click_back_btn()
        page.press_back()
        page.profile.open_favorites()
        page.favorites.open_item('Pets')
        page.favorites.check_name(pet_name)

    @allure.title("Добавление в избранное place")
    @pytest.mark.smoke
    @pytest.mark.favorites
    def test_add_to_favorite_place(self, authorization):
        page = MainPage()
        page.profile.open_places()
        page.place.click_add_new_place()
        place_name = page.place.create_new_place()
        page.place.open_place(place_name)
        page.add_to_favorite()
        page.favorites.favorite_btn_wait_color()
        page.click_back_btn()
        page.press_back()
        page.profile.open_favorites()
        page.favorites.open_item('Places')
        page.favorites.check_name(place_name)





