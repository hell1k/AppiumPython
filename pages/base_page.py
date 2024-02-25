import time

import allure
import uiautomator2 as u


class BasePage:
    d = u.connect("emulator-5554")

    def click(self, locator, element_name=None):
        if element_name is not None:
            with allure.step("Клик по элементу '{element_name}'"):
                self.get_element(locator).click()
        else:
            self.get_element(locator).click()

    def set_text(self, locator, text, element_name=None):
        if element_name is not None:
            with allure.step("Заполнение поля '{element_name}' текстом '{text}'"):
                self.get_element(locator).set_text(text)
        else:
            self.get_element(locator).set_text(text)

    def get_element(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            return self.d.xpath(locator)
        else:
            return self.d(resourceId=locator)

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

    @allure.step("Свайп")
    def swipe_down(self):
        self.d.swipe(400, self.d.window_size()[1]/2, 400, self.d.window_size()[1]/4)

