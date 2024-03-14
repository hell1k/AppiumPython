import random
import time

import allure
import uiautomator2 as u


class BasePage:
    d = u.connect("emulator-5554")

    def click(self, locator, element_name=None):
        if not isinstance(locator, str):
            if element_name is not None:
                with allure.step(f"Клик по элементу '{element_name}'"):
                    locator.click()
                    self.wait_a_moment()
                    self.get_screen()
            else:
                locator.click()
                self.wait_a_moment()
                self.get_screen()
        else:
            if element_name is not None:
                with allure.step(f"Клик по элементу '{element_name}'"):
                    self.get_element(locator).click()
                    self.wait_a_moment()
                    self.get_screen()
            else:
                self.get_element(locator).click()
                self.wait_a_moment()
                self.get_screen()

    def set_text(self, locator, text, element_name=None):
        if element_name is not None:
            with allure.step(f"Заполнение поля '{element_name}' текстом '{text}'"):
                self.get_element(locator).set_text(text)
        else:
            self.get_element(locator).set_text(text)

    def get_element(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            return self.d.xpath(locator)
        else:
            return self.d(resourceId=locator)

    def get_random_element(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            counter = random.randrange(0, len(self.d.xpath(locator)))
            return self.d.xpath(locator)[counter]
        else:
            counter = random.randrange(0, len(self.d(resourceId=locator)))
            return self.d(resourceId=locator)[counter]

    def get_text(self, locator):
        return self.get_element(locator).get_text()

    def wait_a_moment(self):
        time.sleep(0.5)

    def wait_a_second(self):
        time.sleep(1)

    def get_screen(self):
        screen = "screen.png"
        self.d.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)

    @allure.step("Свайп вверх")
    def swipe_up(self):
        self.d.swipe(self.d.window_size()[0] / 2, self.d.window_size()[1] / 2, self.d.window_size()[0] / 2,
                     self.d.window_size()[1] / 4)

    @allure.step("Свайп вниз")
    def swipe_down(self):
        self.d.swipe(self.d.window_size()[0] / 2, self.d.window_size()[1] / 4, self.d.window_size()[0] / 2,
                     self.d.window_size()[1] / 2)

    def wait_element(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Ожидание элемента '{element_name}'"):
                self.get_element(locator).wait(timeout=10)
                # assert self.get_element(locator).exists == True, print(element_name + " отсутствует")
        else:
            self.get_element(locator).wait(timeout=10)
            # assert self.get_element(locator).exists == True

    def checking_exists_element(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Ожидание элемента '{element_name}'"):
                assert self.get_element(locator).exists == True, print(element_name + " отсутствует")
        else:
            assert self.get_element(locator).exists == True

    @allure.step('Press back')
    def press_back(self):
        self.d.press('back')
