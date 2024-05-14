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
    tab_layout = '//*[@resource-id="com.yapmap.yapmap:id/tab_layout"]'
    i_own = '//*[@resource-id="com.yapmap.yapmap:id/owner_layout"]'
    i_am_interested = '//*[@resource-id="com.yapmap.yapmap:id/member_layout"]'

    def click_people_tab(self):
        self.click(self.people_tab, 'вкладка People')

    def click_pets_tab(self):
        self.swipe_to_element_in_tab(self.pets_tab)
        self.click(self.pets_tab, 'вкладка Pets')

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





