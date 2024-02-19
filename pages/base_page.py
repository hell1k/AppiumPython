import allure
import uiautomator2 as u
from uiautomator2 import Initer, ConnectError

d = u.connect("emulator-5554")


class BasePage:

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
            return d.xpath(locator)
        else:
            return d(resourceId=locator)

    def get_text(self, locator):
        return self.get_element(locator).get_text()


