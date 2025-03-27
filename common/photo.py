import allure

from pages.base_page import BasePage
from common.permission import Permission


class Photo(BasePage):
    add_photo_btn = 'com.yapmap.yapmap:id/photos_field_add_photo_text_view'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/avatar_layout"]/android.widget.FrameLayout[1]'
    done_photo = "com.yapmap.yapmap:id/action_done"


    @allure.step("Добавление нового фото")
    def upload_new_photo(self, permission=True):
        if permission == True:
            Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        if permission == True:
            Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.wait_a_second()
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.wait_a_second()
        self.click(self.done_photo, 'кнопка Done')

    @allure.step("Добавление нового фото")
    def upload_picture(self, permission=True):
        if permission:
            Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        if permission:
            Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.wait_a_second()
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.wait_a_second()

