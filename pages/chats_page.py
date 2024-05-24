import time
from random import randint

import allure
import random
from tests.config import *
from pages.base_page import BasePage
from common.menu import Menu
from common.permission import Permission


class ChatsPage(BasePage):
    menu = Menu()

    people_tab = '//*[@text="People"]'
    pets_tab = '//*[@text="Pets"]'
    market_tab = '//*[@text="Market"]'
    business_tab = '//*[@text="Businesses"]'
    jobs_tab = '//*[@text="Jobs"]'
    tab_layout = '//*[@resource-id="com.yapmap.yapmap:id/tab_layout"]'
    i_own = '//*[@resource-id="com.yapmap.yapmap:id/owner_layout"]'
    i_am_interested = '//*[@resource-id="com.yapmap.yapmap:id/member_layout"]'
    business_chats = '//*[@resource-id="com.yapmap.yapmap:id/business_chats_recycler_view"]/android.widget.LinearLayout'

    def click_people_tab(self):
        self.click(self.people_tab, 'вкладка People')

    def click_pets_tab(self):
        self.swipe_to_element_in_tab(self.pets_tab)
        self.click(self.pets_tab, 'вкладка Pets')

    def click_market_tab(self):
        self.swipe_to_element_in_tab(self.market_tab)
        self.click(self.market_tab, 'вкладка Market')

    def click_business_tab(self):
        self.wait_a_second()
        self.wait_a_second()
        self.swipe_to_element_in_tab(self.business_tab)
        self.click(self.business_tab, 'вкладка Pets')

    def click_jobs_tab(self):
        self.swipe_to_element_in_tab(self.jobs_tab)
        self.click(self.jobs_tab, 'вкладка Jobs')

    def check_pets_message(self, pet_name, user_pet_name, message):
        self.click_pets_tab()
        self.click(self.i_own)
        self.click(f'//*[@text="{pet_name}"]', pet_name)
        self.wait_a_second()
        self.click(f'//*[@text="{user_pet_name}"]', user_pet_name)
        self.wait_a_second()
        self.wait_text(message)

    def swipe_horizontal_tabs(self):
        fx, fy = self.get_element(self.tab_layout).center()
        tx, ty = self.get_element(self.people_tab).center()
        self.swipe_coordinate(fx, fy, tx, ty)

    def swipe_to_element_in_tab(self, locator):
        for i in range(3):
            if self.get_elements_amount(locator) == 0:
                self.swipe_horizontal_tabs()
                self.wait_a_second()
            else:
                self.wait_element(locator)
                break

    def check_business_message(self, business_name, new_message):
        self.click_business_tab()
        self.click(self.i_own)
        self.click(self.business_chats)
        self.wait_text(business_name)
        self.wait_a_second()
        self.wait_text(new_message)

    def check_job_message(self, position_name, message):
        self.click_jobs_tab()
        self.click(self.i_own)
        self.click(f'//*[@text="{position_name}"]', position_name)
        self.wait_a_second()
        self.wait_text(message)

    def check_market_message(self, message):
        self.click_market_tab()
        self.click(self.i_own)
        self.wait_text(message)
        self.click(f'//*[@text="{message}"]')
        self.wait_text(message)





