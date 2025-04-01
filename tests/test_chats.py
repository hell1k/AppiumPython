import allure
import pytest

from pages.main_page import MainPage
from tests.config import *


@pytest.mark.usefixtures("setup")
@allure.feature("Chats")
class TestChats:
    @allure.title("Проверка добавления и удаления стикер пака новым пользователем")
    @pytest.mark.smoke
    @pytest.mark.chats
    def test_add_and_del_sticker_pack(self):
        page = MainPage()
        page.login.registration()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        new_message = faker.text()
        page.channels.send_message(new_message)
        page.chats.checking_comment()
        page.chats.add_sticker_pack_comment()
        page.chats.check_send_sticker()
        page.chats.del_sticker_pack()

    @allure.title("Проверка открытия разделов на экране Chats")
    @pytest.mark.smoke
    @pytest.mark.chats
    def test_open_chats_tabs(self):
        page = MainPage()
        page.login.registration()
        page.menu.open_chats()
        page.chats.checking_clear_chat()

    @allure.title("Проверка отправки всех типов медиа в чат BUSINESS")
    @pytest.mark.smoke
    @pytest.mark.business
    @pytest.mark.chats
    # @pytest.mark.login_marker("yapmap.tester+chats@yandex.ru")
    def test_business_chat(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.clear_business()
        business_name = page.business.add_new_business()
        page.wait_text(business_name)
        page.business.click_back_btn()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.select_local_deals_filter()
        page.open_bottom_sheet()
        page.business.user_open_business(business_name)
        page.business.user_check_business()
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_attachment()
        new_message = page.business.test_chat()
        page.login.logout()
        page.login.authorization()
        page.menu.open_chats()
        page.chats.check_business_message(business_name, new_message)

    @allure.title("Проверка отправки всех типов медиа в чат CHANNELS и очистка чата")
    @pytest.mark.smoke
    @pytest.mark.channels
    @pytest.mark.chats
    # @pytest.mark.login_marker("yapmap.tester+chats@yandex.ru")
    def test_channels_chat(self, authorization):
        page = MainPage()
        page.menu.open_channels()
        channel_name = page.channels.add_new_channel()
        page.channels.open_channel(channel_name)
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images_type_2()
        page.chats.check_send_attachment()
        new_message = faker.text()
        page.channels.send_message(new_message)
        page.click_back_btn()
        page.click_back_btn()
        page.channels.open_channel(channel_name)
        page.chats.check_message_in_chat(new_message)
        page.click_back_btn()
        page.channels.open_channel(channel_name)
        page.chats.check_message_in_chat(new_message)
        page.channels.click_edit_channel()
        page.swipe_to_element(page.channels.clear_chat_history_btn)
        page.channels.clear_chat_history()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_channels()
        page.channels.open_channel(channel_name)
        page.channels.checking_empty_chat()

    @allure.title("Проверка отправки всех типов медиа в чат EVENTS и очистка чата")
    @pytest.mark.smoke
    @pytest.mark.events
    @pytest.mark.chats
    # @pytest.mark.login_marker("yapmap.tester+chats@yandex.ru")
    def test_event_chat(self, authorization):
        page = MainPage()
        page.profile.open_events()
        event_name = page.events.add_new_event()
        page.events.user_open_event(event_name)
        page.events.checking_chat_btn()
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images()
        page.chats.check_send_attachment()
        new_message = faker.text()
        page.events.send_message(new_message)
        page.chats.back_from_chat_to_main()
        page.wait_a_second()
        page.click_back_btn()
        page.wait_a_second()
        page.click_back_btn()
        page.menu.open_chats()
        page.chats.open_events_tab()
        page.events.open_event(event_name)
        page.chats.check_message_in_chat(new_message)
        page.events.click_edit()
        page.swipe_to_element(page.events.clear_chat_history_btn)
        page.events.clear_chat_history()
        page.events.checking_empty_chat()
        page.click_back_btn()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.events.user_open_event(event_name)
        page.events.checking_empty_chat()

    @allure.title("Проверка отправки всех типов медиа в чат GROUPS и очистка чата")
    @pytest.mark.smoke
    @pytest.mark.groups
    @pytest.mark.chats
    # @pytest.mark.login_marker("yapmap.tester+chats@yandex.ru")
    def test_groups_chat(self, authorization):
        page = MainPage()
        page.menu.open_groups()
        group_name = page.groups.add_new_group()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_groups()
        page.groups.join_an_open_group(group_name)
        page.groups.click_chat_icon()
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images()
        page.chats.check_send_attachment()
        new_message = faker.text()
        page.groups.send_message(new_message)
        page.chats.back_from_chat()
        page.menu.open_chats()
        page.chats.open_groups_tab()
        page.groups.open_an_open_group(group_name)
        page.chats.check_message_in_chat(new_message)
        page.chats.back_from_chat()
        page.login.logout()
        page.login.authorization()
        page.menu.open_groups()
        page.groups.open_an_open_group(group_name)
        page.groups.click_edit_group()
        page.groups.clear_chat_history()
        page.press_back()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.menu.open_groups()
        page.groups.open_an_open_group(group_name)
        page.groups.checking_empty_chat()

    @allure.title("Проверка отправки всех типов медиа в чат JOBS")
    @pytest.mark.smoke
    @pytest.mark.jobs
    @pytest.mark.chats
    # @pytest.mark.login_marker("yapmap.tester+chats@yandex.ru")
    def test_jobs_chat(self, authorization):
        page = MainPage()
        page.profile.open_business()
        page.business.check_business_item_availability()
        page.business.click_back_btn()
        page.profile.click_jobs()
        position_name = page.jobs.create_new_jobs()

        page.jobs.click_back_btn()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.wait_a_second()
        page.swipe_coordinate(100, 500, 1300, 1000)
        page.wait_a_second()
        page.open_bottom_sheet_a_bit()
        page.select_jobs_filter()
        # page.open_bottom_sheet()
        page.jobs.user_open_job(position_name)
        page.jobs.add_to_favorite()
        page.jobs.checking_more_options_user()
        page.jobs.click_contact_employer()
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images()
        page.chats.check_send_attachment()
        message = page.jobs.test_chat()
        page.menu.open_chats()
        page.chats.open_jobs_tab()
        page.chats.click_i_am_interested()
        page.jobs.open_job(position_name)
        page.chats.check_message_in_chat(message)
        page.chats.back_from_chat()
        page.login.logout()
        page.login.authorization()
        page.menu.open_chats()
        page.chats.check_job_message(position_name, message)
        page.jobs.click_delete_and_leave(position_name)

    @allure.title("Проверка отправки всех типов медиа в чат MARKET")
    @pytest.mark.smoke
    @pytest.mark.market
    @pytest.mark.chats
    # @pytest.mark.login_marker("yapmap.tester+chats@yandex.ru")
    def test_market_chat(self, authorization):
        # Создаем объявление пользователем 1
        page = MainPage()
        page.profile.open_market()
        page.market.click_plus_new_market()
        page.market.click_create()
        ad_name = page.market.create_new_ad_stuff()
        page.pets.click_back_btn()
        page.login.logout()
        # Открываем объявление пользователем 2 и отправляем сообщение пользователю 1
        page.login.authorization(test_user_login, test_user_password)
        page.wait_a_second()
        page.wait_a_second()
        page.swipe_coordinate(100, 500, 1300, 1000)
        page.wait_a_second()
        page.open_bottom_sheet_a_bit()
        # page.open_bottom_sheet()
        page.select_market_filter()
        page.user_open_ad(ad_name)
        page.market.checking_more_options_user()
        page.market.add_to_favorite()
        page.market.click_contact_seller_btn()
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images()
        page.chats.check_send_attachment()
        message = page.chats.check_send_text()
        page.chats.back_from_chat_to_main()
        page.menu.open_chats()
        page.chats.open_market_tab()
        # page.chats.click_i_am_interested()
        page.chats.open_item_by_name(ad_name) # другое значение в ad_name
        page.chats.check_message_in_chat(message)
        # page.login.logout()
        # Открываем объявление пользователем 1 и проверяем сообщение от пользователя 2
        # page.login.authorization()
        # page.menu.open_chats()
        # page.chats.check_market_message(message)
        # new_message = faker.text()
        # page.market.send_message(new_message)

    @allure.title("Проверка отправки всех типов медиа в чат PETS")
    @pytest.mark.smoke
    @pytest.mark.pets
    @pytest.mark.debug
    # @pytest.mark.login_marker("yapmap.tester+chats@yandex.ru")
    def test_pets_chat(self, authorization):
        # Создаем питомца пользователем 1
        page = MainPage()
        page.profile.open_pets()
        page.pets.add_new_pet_btn()
        page.pets.click_ok()
        page.pets.add_photo()
        pet_name = page.pets.add_new_pet()
        page.press_back()
        page.pets.check_pet_in_list(pet_name)
        page.pets.click_back_btn()
        page.login.logout()
        # Создаем питомца пользователем 2
        page.login.authorization(test_user_login, test_user_password)
        page.profile.open_pets()
        page.pets.add_new_pet_btn()
        page.pets.click_ok()
        page.pets.add_photo()
        user_pet_name = page.pets.add_new_pet()
        # Открываем пользователем 2 питомца пользователя 1
        page.pets.wait_pets_page()
        # page.press_back()
        page.press_back()
        page.menu.open_search()
        page.select_pets_filter()
        page.swipe_coordinate(100, 500, 1300, 1000)
        page.wait_a_second()
        page.open_bottom_sheet_a_bit()
        # page.open_bottom_sheet()
        page.pets.search_pet_name(pet_name) # Не находит никаких pet
        page.pets.open_pet(pet_name)
        page.pets.checking_more_options_user()
        page.pets.add_to_favorite()
        # Отправляем сообщение питомцу 1 от питомца 2
        page.pets.click_send_message()
        page.pets.open_pet(user_pet_name)
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images()
        page.chats.check_send_attachment()
        message = page.pets.test_chat()
        page.menu.open_chats()
        page.chats.open_pets_tab()
        page.chats.click_i_am_interested()
        page.chats.open_item_by_name(pet_name)
        page.chats.check_message_in_chat(message)
        page.click_back_btn()
        page.login.logout()
        # Проверяем что пользователь 1 увидит сообщение пользователя 2
        page.login.authorization()
        # Путь проверки - 'Профиль - Чат - Pets - I own - name_pet - user_pet_name'
        page.menu.open_chats()
        page.chats.check_pets_message(pet_name, user_pet_name, message)

    @allure.title("Проверка отправки всех типов медиа в чат PLACE")
    @pytest.mark.smoke
    @pytest.mark.place
    @pytest.mark.chats
    # @pytest.mark.login_marker("yapmap.tester+chats@yandex.ru")
    def test_place_chat(self, authorization):
        page = MainPage()
        page.profile.open_places()
        page.place.click_add_new_place()
        place_name = page.place.create_new_place()
        page.place.open_place(place_name)
        page.place.click_group_chat_btn(place_name)
        # page.chats.check_send_emoji()
        # page.chats.check_send_sticker()
        page.chats.check_send_images_from_camera()
        page.chats.check_send_images()
        page.chats.check_send_attachment()
        message = page.place.test_chat()
        page.place.click_back_btn()
        page.place.click_back_btn()
        page.menu.open_chats()
        page.chats.open_places_tab()
        # page.chats.click_i_own()
        page.chats.open_item_by_name(place_name)
        page.chats.check_message_in_chat(message)
        page.chats.back_from_chat()
        page.login.logout()
        page.login.authorization(test_user_login, test_user_password)
        page.open_bottom_sheet()
        page.select_places_filter()
        page.close_bottom_sheet()
        page.swipe_coordinate(100, 1000, 1200, 1000)
        page.wait_a_second()
        page.swipe_coordinate(500, 300, 500, 800)
        page.open_bottom_sheet_a_bit()
        page.wait_element('com.yapmap.yapmap:id/name_text_view')
        page.open_bottom_sheet()
        page.user_open_place(place_name)
        page.place.checking_more_options_user_place(place_name)
        page.place.add_to_favorite()
        page.place.click_group_chat_btn(place_name)
        # page.place.check_chat_msg(message)
        # new_message = page.place.test_chat()
        # page.place.click_back_btn()
        # page.place.click_back_btn()
        # page.login.logout()
        # page.login.authorization()
        # page.profile.open_places()
        # page.user_open_place(place_name)
        # page.place.click_group_chat_btn(place_name)
        # page.place.check_chat_msg(new_message)