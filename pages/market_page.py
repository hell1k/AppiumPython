import random

import allure
import faker
from faker import Faker
from common.menu import Menu
from common.permission import Permission
from pages.base_page import BasePage
from tests.config import *


class MarketPage(BasePage):
    menu = Menu()
    faker = Faker()

    plus_market_btn = 'com.yapmap.yapmap:id/action_create'
    create_btn = 'com.yapmap.yapmap:id/create_button'
    cancel_button = "com.yapmap.yapmap:id/cancel_button"
    create_button = "com.yapmap.yapmap:id/create_button"
    type_switch_sale_rent = "com.yapmap.yapmap:id/type_switch"
    transportation_type = "com.yapmap.yapmap:id/transportation_text_view"
    stuff_type = "com.yapmap.yapmap:id/item_text_view"
    housing_type = "com.yapmap.yapmap:id/housing_text_view"
    add_photo_btn = 'com.yapmap.yapmap:id/photos_field_add_photo_text_view'
    image_loader = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[1]'
    take_a_picture_btn = 'com.android.camera2:id/bottom_bar'
    take_a_picture_done_btn = '//*[@resource-id="com.android.camera2:id/done_button"]'
    upload_a_picture = '//*[@resource-id="com.yapmap.yapmap:id/avatar_layout"]/android.widget.FrameLayout[1]'
    title_field = "com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"
    done_photo = "com.yapmap.yapmap:id/action_done"
    category_selection = '//*[@text="Category"]/..'
    type_selection = '//*[@text="Type"]/..'
    zip_selector = '//*[@text="ZIP"]/..'
    price_selector = '//*[@text="Price"]/..'
    location_selector = '//*[@text="Location"]/..'
    currency_selector = '//*[@text="Currency"]/..'

    type_of_transport = '//*[@text="Type of transport"]/..'
    make = '//*[@text="Make"]/..'
    year = '//*[@text="Year"]/..'
    body_type = '//*[@text="Body type"]/..'
    trim = '//*[@text="Trim"]/..'
    engine_cylinders = '//*[@text="Engine cylinders"]/..'
    liters = '//*[@text="Liters"]/..'
    fuel_type = '//*[@text="Fuel type"]/..'
    transmission = '//*[@text="Transmission"]/..'
    drivetrain = '//*[@text="Drivetrain"]/..'
    interior = '//*[@text="Interior"]/..'
    condition = '//*[@text="Condition"]/..'
    exterior_color = '//*[@text="Exteriror color"]/..'
    interior_color = '//*[@text="Interior color"]/..'
    sunroof_moonroof = '//*[@text="Sunroof / moonroof"]/..'
    alloy_wheels = '//*[@text="Alloy wheels"]/..'
    third_row_seating = '//*[@text="Third row seating"]/..'
    bluetooth = '//*[@text="Bluetooth"]/..'
    backup_camera = '//*[@text="Backup camera"]/..'
    parking_sensors = '//*[@text="Parking sensors"]/..'
    remote_start = '//*[@text="Remote start"]/..'
    heated_seats = '//*[@text="Heated seats"]/..'
    quick_order_package = '//*[@text="Quick order package"]/..'
    do_you_have_a_clear_title = '//*[@text="Do You Have a Clear Title?"]/..'
    has_your_car_ever_been_in_an_accident = '//*[@text="Has Your Car Ever Been in an Accident?"]/..'
    does_your_car_have_cosmetic_or_mechanical_issues = '//*[@text="Does Your Car Have Cosmetic or Mechanical Issues?"]/..'
    does_your_car_run_and_drive = '//*[@text="Does your car run and drive?"]/..'
    is_there_history = '//*[@text="Is there history on your vehicle resulting from flood, theft recovery or salvage loss?"]/..'
    serial_number = '//*[@text="Serial number"]/..'
    model = '//*[@text="Model"]/..'
    mileage ='//*[@text="Mileage, mi"]/..'
    vin_code = '//*[@text="VIN-code"]/..'
    working_hours = '//*[@text="Working hours"]/..'

    property_type = '//*[@text="Property type"]/..'
    year_built = '//*[@text="Year built"]/..'
    bedrooms = '//*[@text="Bedrooms"]/..'
    bathrooms = '//*[@text="Bathrooms"]/..'
    basement = '//*[@text="Basement"]/..'
    pool = '//*[@text="Pool"]/..'
    parking_spots_number = '//*[@text="Parking spots number"]/..'
    parking_type = '//*[@text="Parking type"]/..'
    laundry_type = '//*[@text="Laundry type"]/..'
    air_condition_type = '//*[@text="Air condition type"]/..'
    heating_type = '//*[@text="Heating type"]/..'
    pets_ok = '//*[@text="Pets OK"]/..'
    living_area = '//*[@text="Living area"]/..'
    lot_size = '//*[@text="Lot size"]/..'

    shipping_available_switch = '//*[@text="Shipping available"]/..'
    exchange_is_possible_switch = '//*[@text="Exchange is possible"]/..'
    bargaining_is_possible_switch = '//*[@text="Bargaining is possible"]/..'
    types = '//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout'
    type_address_field = "com.yapmap.yapmap:id/auto_complete_text_view"
    address_popup = '//*[@text="Novosibirsk, Novosibirsk Oblast, Russia"]'
    map_plus_btn = '//*[@resource-id="com.yapmap.yapmap:id/floating_action_button"]'
    edit_text_view = "com.yapmap.yapmap:id/edit_text_view"
    description_field = '//*[@resource-id="com.yapmap.yapmap:id/relagram_input_edit_text_field_edit_text"]'
    post_button = '//*[@resource-id="com.yapmap.yapmap:id/post_button"]'
    done_button = "com.yapmap.yapmap:id/done_button"
    add_to_favorites_btn = 'com.yapmap.yapmap:id/action_add_to_favourites'
    more_options = '//*[@content-desc="More options"]'
    qr_code = 'com.yapmap.yapmap:id/qr_code_image_view'
    pop_up_ok_btn = "com.yapmap.yapmap:id/ok_button"
    share_text = '//*[@resource-id="android:id/content_preview_text" and contains(@text, "Hey! Look at the advertisement")]'
    first_photo = '//*[@resource-id="com.yapmap.yapmap:id/images_recycler_view"]/android.view.ViewGroup[2]'
    switch_compat = "com.yapmap.yapmap:id/switch_compat"
    enter_manually_button = "com.yapmap.yapmap:id/enter_manually_button"
    vin_code_edit_text = "com.yapmap.yapmap:id/vin_code_edit_text"
    use_vin_code_image_view = "com.yapmap.yapmap:id/use_vin_code_image_view"

    def click_back_btn(self):
        self.click(self.d(description="Back"), "кнопка Назад")

    def click_plus_new_market(self):
        self.wait_a_second()
        self.click(self.plus_market_btn, "кнопка + создания новой сущности Market")
        self.wait_a_second()

    def click_create(self):
        self.wait_a_second()
        self.click(self.create_btn, "кнопка Create")

    @allure.step("Добавление в избранное")
    def add_to_favorite(self):
        self.wait_a_second()
        self.click(self.add_to_favorites_btn, "кнопка добавления в избранное")
        self.wait_a_second()

    @allure.step("Переход в доп опции '{option_name}'")
    def open_more_options(self, option_name):
        self.click(self.more_options, "меню группы")
        self.click(f'//*[@text="{option_name}"]', option_name)

    def check_create_buttons(self):
        self.click_plus_new_market()
        self.wait_text('Create an ad')
        self.click_back_btn()
        self.click_create()
        self.wait_text('Create an ad')
        self.click(self.cancel_button, 'кнопка Cancel')

    @allure.step("Выбор типа transportation")
    def select_transportation_type_ad(self):
        self.click(self.transportation_type)

    @allure.step("Выбор типа transportation")
    def select_stuff_type_ad(self):
        self.click(self.stuff_type)

    @allure.step("Выбор типа transportation")
    def select_housing_type_ad(self):
        self.click(self.housing_type)

    @allure.step("Нажать на свитч Sale/Rent")
    def click_switch_sale_rent(self):
        self.click(self.type_switch_sale_rent)

    @allure.step("Выбор случайного типа")
    def select_random_type_ad(self):
        random_type = random.randrange(1, 3)
        if random_type == 1:
            self.select_transportation_type_ad()
        if random_type == 2:
            self.select_stuff_type_ad()
        if random_type == 3:
            self.select_housing_type_ad()
        random_type = random.randrange(1, 2)
        if random_type == 1:
            self.click_switch_sale_rent()
        else:
            pass

    @allure.step("Добавление нового фото")
    def upload_new_photo(self):
        self.click(self.add_photo_btn, 'add photo')
        Permission().close_photo_permission()
        self.click(self.image_loader, "добавление нового фото")
        Permission().click_while_using_the_app()
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.click(self.done_photo, 'кнопка Done')
        self.wait_a_second()

    @allure.step("Добавление фото")
    def upload_photo(self):
        self.click(self.add_photo_btn, 'add photo')
        Permission().close_photo_permission()
        self.click(self.first_photo)
        self.wait_a_second()
        self.click(self.done_photo, 'кнопка Done')
        self.wait_a_second()

    @allure.step("Добавить фото")
    def add_photo_without_permissions(self):
        self.click(self.add_photo_btn, 'кнопка Add photos')
        self.click(self.image_loader, "добавление нового фото")
        self.wait_element(self.take_a_picture_btn)
        self.wait_a_second()
        self.click(self.take_a_picture_btn, "создание нового фото")
        self.click(self.take_a_picture_done_btn, "выбрать фото")
        self.wait_a_second()
        self.click(self.done_photo, 'кнопка Done')

    @allure.step("Заполнение поля Advertisement name")
    def set_ad_name(self):
        self.swipe_to_element(self.title_field)
        ad_name = 'Test AD_'+ str(random.randint(0, 999999999999))
        self.set_text(self.title_field, ad_name, "Advertisement name")
        return ad_name

    @allure.step("Выбор случайного типа")
    def select_random(self):
        self.wait_element(self.types)
        self.click(self.get_random_element(self.types), "рандомный тип")
        self.wait_a_moment()

    @allure.step("Выбрать адрес")
    def set_address(self, city_name='Novosibirsk'):
        self.wait_text('Choose location')
        self.set_text(self.type_address_field, city_name)
        self.click(self.address_popup, 'адрес из всплывашки')
        self.click(self.map_plus_btn, 'кнопка + на карте')

    @allure.step("Создание нового Ad")
    def create_new_ad(self):
        self.click_create()
        self.select_random_type_ad()
        self.click_create()
        self.upload_new_photo()
        self.set_ad_name()
        self.swipe_to_element(self.category_selection)
        self.click(self.category_selection, 'пункт Category')
        self.select_random()
        self.swipe_to_element(self.type_selection)
        self.click(self.type_selection, 'пункт Type')
        self.select_random()

    @allure.step("Создание нового Ad Stuff")
    def create_new_ad_stuff(self, permissions=True):
        if permissions == True:
            self.upload_new_photo()
        else:
            self.add_photo_without_permissions()

        ad_name = self.set_ad_name()
        self.swipe_to_element(self.category_selection)
        self.click(self.category_selection, 'пункт Category')
        self.select_random()

        try:
            self.click(self.type_selection, 'пункт Type')
            self.select_random()
        except:
            print('Нет раздела Type для выбранной категории')

        self.swipe_to_element(self.location_selector)
        self.click(self.location_selector, 'пункт Location')
        self.set_address()

        self.swipe_to_element(self.price_selector)
        self.click(self.price_selector, 'Price')
        random_price = random.randrange(1, 10000)
        self.set_text(self.edit_text_view, random_price)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.shipping_available_switch)
        self.click(self.shipping_available_switch, 'свитч Shipping available')
        self.swipe_to_element(self.exchange_is_possible_switch)
        self.click(self.exchange_is_possible_switch, 'свитч Exchange is possible')
        self.swipe_to_element(self.bargaining_is_possible_switch)
        self.click(self.bargaining_is_possible_switch, 'свитч Bargaining is possible')

        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_1000)

        self.swipe_to_element(self.post_button)
        self.click(self.post_button, 'кнопка Post')

        self.wait_text('Market')
        self.swipe_down()
        self.wait_a_second()
        self.wait_a_second()
        self.wait_text(ad_name)
        return ad_name

    @allure.step("Создание нового Ad Transport")
    def create_new_ad_transport(self):
        self.upload_photo()
        ad_name = self.set_ad_name()

        # Basic information
        self.swipe_to_element(self.type_of_transport)
        self.click(self.type_of_transport, 'пункт Type of transport')
        self.select_random()
        self.swipe_up()

        try:
            self.click(self.vin_code, 'VIN-code')
            self.wait_a_second()
            Permission().click_while_using_the_app()
            self.wait_a_second()
            self.click(self.enter_manually_button, 'кнопка ENTER MANUALLY')
            self.wait_a_second()
            self.set_text(self.vin_code_edit_text, 'THMBB7092WD114221')
            self.click(self.use_vin_code_image_view, 'подтвердить VIN code')
        except:
            print('Нет раздела Serial number для выбранного типа транспорта')

        try:
            self.click(self.serial_number, 'Serial number')
            random_serial_number = random.randrange(1, 10000)
            self.set_text(self.edit_text_view, random_serial_number)
            self.click(self.done_button, 'кнопка Done')
        except:
            print('Нет раздела Serial number для выбранного типа транспорта')

        self.swipe_to_element(self.make)
        self.click(self.make, 'пункт Make')
        self.select_random()

        try:
            self.swipe_to_element(self.model)
            self.click(self.model, 'пункт Model')
            # self.select_random()
            self.click('//*[@text="Other"]/../..')
        except:
            print('Нет раздела Model для выбранного типа транспорта')

        self.swipe_to_element(self.year)
        self.click(self.year, 'пункт Year')
        # self.set_year()
        self.click(self.done_button, 'кнопка Done')

        try:
            self.click(self.body_type, 'пункт Body type')
            self.select_random()
        except:
            print('Нет раздела Body type для выбранного типа транспорта')

        self.swipe_to_element(self.trim)
        self.wait_a_second()
        self.click(self.trim, 'Trim')
        text = 'Simple trim text'
        self.set_text(self.edit_text_view, text)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_up()
        self.wait_a_second()
        try:
            self.click(self.mileage, 'Mileage, mi')
            random_mileage = random.randrange(1, 150000)
            self.set_text(self.edit_text_view, random_mileage)
            self.click(self.switch_compat, 'свитч Мили/Километры')
            self.click(self.done_button, 'кнопка Done')

        except:
            print('Нет раздела Miliage для выбранного типа транспорта')
        self.wait_a_second()
        try:
            self.click(self.working_hours, 'Working hours')
            random_hours = random.randrange(1, 1500)
            self.set_text(self.edit_text_view, random_hours)
            self.click(self.done_button, 'кнопка Done')
        except:
            print('Нет раздела Miliage для выбранного типа транспорта')

        self.swipe_to_element(self.location_selector)
        self.click(self.location_selector, 'пункт Location')
        self.set_address()

        self.swipe_to_element(self.price_selector)
        self.click(self.price_selector, 'Price')
        random_price = random.randrange(1, 10000)
        self.set_text(self.edit_text_view, random_price)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.exchange_is_possible_switch)
        self.click(self.exchange_is_possible_switch, 'свитч Exchange is possible')
        self.swipe_to_element(self.bargaining_is_possible_switch)
        self.click(self.bargaining_is_possible_switch, 'свитч Bargaining is possible')

        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_1000)

        # Additional characteristics
        self.swipe_to_element(self.engine_cylinders)
        self.click(self.engine_cylinders, 'пункт engine_cylinders')
        self.select_random()

        self.swipe_to_element(self.liters)
        self.click(self.liters, 'пункт Liters')
        random_liters = random.randrange(1, 6)
        self.set_text(self.edit_text_view, random_price)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.fuel_type)
        self.click(self.fuel_type, 'пункт Fuel type')
        self.select_random()

        self.swipe_to_element(self.transmission)
        self.click(self.transmission, 'пункт Transmission')
        self.select_random()

        # ...

        self.swipe_to_element(self.post_button)
        self.click(self.post_button, 'кнопка Post')

        self.wait_text('Market')
        self.swipe_down_to_element(f'//*[@text="{ad_name}"]')
        self.wait_a_second()
        self.wait_text(ad_name)
        return ad_name

    @allure.step("Создание нового Ad Housing")
    def create_new_ad_housing(self, permissions=True):
        if permissions == True:
            self.upload_new_photo()
        else:
            self.add_photo_without_permissions()

        ad_name = self.set_ad_name()

        self.swipe_to_element(self.property_type)
        self.click(self.property_type)
        self.select_random()

        self.swipe_to_element(self.year_built)
        self.click(self.year_built)
        self.set_random_year()

        self.swipe_to_element(self.location_selector)
        self.click(self.location_selector, 'пункт Location')
        self.set_address()

        self.swipe_to_element(self.price_selector)
        self.click(self.price_selector, 'Price')
        random_price = random.randrange(1, 10000)
        self.set_text(self.edit_text_view, random_price)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.exchange_is_possible_switch)
        self.click(self.exchange_is_possible_switch, 'свитч Exchange is possible')
        self.swipe_to_element(self.bargaining_is_possible_switch)
        self.click(self.bargaining_is_possible_switch, 'свитч Bargaining is possible')

        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_1000)

        self.swipe_to_element(self.bedrooms)
        self.click(self.bedrooms, 'Bedrooms')
        random_bedrooms = random.randrange(1, 12)
        self.set_text(self.edit_text_view, random_bedrooms)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.bathrooms)
        self.click(self.bathrooms, 'Bathrooms')
        random_bathrooms = random.randrange(1, 12)
        self.set_text(self.edit_text_view, random_bathrooms)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.basement)
        self.click(self.basement, 'Basement')

        self.swipe_to_element(self.pool)
        self.click(self.pool, 'Pool')

        self.swipe_to_element(self.parking_spots_number)
        self.click(self.parking_spots_number, 'Parking spots number')
        random_number = random.randrange(1, 12)
        self.set_text(self.edit_text_view, random_number)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.parking_type)
        self.click(self.parking_type)
        self.select_random()

        self.swipe_to_element(self.laundry_type)
        self.click(self.laundry_type)
        self.select_random()

        self.swipe_to_element(self.air_condition_type)
        self.click(self.air_condition_type)
        self.select_random()

        self.swipe_to_element(self.heating_type)
        self.click(self.heating_type)
        self.select_random()

        self.swipe_to_element(self.pets_ok)
        self.click(self.pets_ok, 'Pets OK')

        self.click(self.living_area, 'Living area')
        random_area = random.randrange(1, 1500)
        self.set_text(self.edit_text_view, random_area)
        self.click(self.switch_compat, 'свитч sq.Meters/sq.Feet')
        self.click(self.done_button, 'кнопка Done')

        self.click(self.lot_size, 'Lot size')
        random_size = random.randrange(1, 1500)
        self.set_text(self.edit_text_view, random_size)
        self.click(self.switch_compat, 'свитч Hectares/Acres')
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.condition)
        self.click(self.condition, 'Condition')
        self.set_condition()

        self.swipe_to_element(self.post_button)
        self.click(self.post_button, 'кнопка Post')

        self.wait_text('Market')
        self.swipe_down()
        self.wait_a_second()
        self.wait_a_second()
        self.wait_text(ad_name)
        return ad_name

    def open_market(self, ad_name):
        self.wait_a_second()
        self.click(
            f'//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout//*[@text="{ad_name}"]')

    @allure.step("Редактирование Ad Stuff")
    def edit_ad(self):
        self.click(self.more_options, 'кнопка ... в верхнем правом углу')
        self.click('//*[@text="Edit"]')
        self.add_photo_without_permissions()
        ad_name = self.set_ad_name()

        self.swipe_to_element(self.category_selection)
        self.click(self.category_selection, 'пункт Category')
        self.select_random()

        try:
            self.click(self.type_selection, 'пункт Type')
            self.select_random()
        except:
            print('Нет раздела Type для выбранной категории')

        self.swipe_to_element(self.location_selector)
        self.click(self.location_selector, 'пункт Location')
        self.set_address()

        self.swipe_to_element(self.price_selector)
        self.click(self.price_selector, 'Price')
        random_price = random.randrange(1, 10000)
        self.set_text(self.edit_text_view, random_price)
        self.click(self.done_button, 'кнопка Done')

        self.swipe_to_element(self.shipping_available_switch)
        self.click(self.shipping_available_switch, 'свитч Shipping available')
        self.swipe_to_element(self.exchange_is_possible_switch)
        self.click(self.exchange_is_possible_switch, 'свитч Exchange is possible')
        self.swipe_to_element(self.bargaining_is_possible_switch)
        self.click(self.bargaining_is_possible_switch, 'свитч Bargaining is possible')

        self.swipe_to_element(self.description_field)
        self.set_text(self.description_field, text_1000_2)

        self.swipe_to_element(self.post_button)
        self.click(self.post_button, 'кнопка Edit')
        self.wait_a_second()
        self.wait_text(ad_name[:14])
        self.click_back_btn()
        self.wait_text('Market')
        self.swipe_down()
        self.wait_a_second()
        self.wait_text(ad_name)

        return ad_name

    @allure.step("Удаление Ad")
    def delete_ad(self, ad_name):
        self.click(self.more_options, 'кнопка ... в верхнем правом углу')
        self.click('//*[@text="Delete"]')
        self.click(self.pop_up_ok_btn, 'кнопка ОК на popup')
        self.swipe_down()
        self.wait_a_second()
        self.d(resourceId='com.yapmap.yapmap:id/recycler_view').child(text=ad_name).wait_gone(10)

    @allure.step("Проверка меню ... в шапке")
    def checking_more_options(self):
        self.wait_a_moment()
        self.open_more_options("Edit")
        self.wait_text('Editing')
        self.wait_a_second()
        self.click_back_btn()
        try:
            self.click('//*[@text="NO"]')
        except:
            print('Иногда при выходе без редактирования предлагает сохранить изменения, сейчас не предложил')
        self.open_more_options("Share")
        self.wait_a_second()
        self.wait_element(self.share_text)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Generate QR Code")
        self.wait_element(self.qr_code)
        self.press_back()
        self.wait_a_moment()
        self.open_more_options("Delete")
        self.wait_text('Delete advertisement')
        self.click(self.cancel_button, 'кнопка Cancel')
        self.wait_hidden_element(self.cancel_button)
        self.add_to_favorite()
        self.click_back_btn()
        self.wait_a_second()

    @allure.step("Выбрать случайный Condition")
    def set_condition(self):
        self.click(f'//*[@resource-id="com.yapmap.yapmap:id/condition{random.randrange(1, 5)}_layout"]')
        self.click(self.done_button, 'кнопка Done')

    @allure.step("Выбрать случайный Year")
    def set_random_year(self):
        count = random.randrange(2, 5)
        f = '//*[@resource-id="com.yapmap.yapmap:id/recycler_view"]/android.widget.LinearLayout[5]'
        t = '//*[@resource-id="com.android.systemui:id/white_cutout"]'
        for i in range(count):
            fx, fy = self.get_element(f).center()
            ty = self.d.window_size()[1] - 10
            tx = self.d.window_size()[0] / 2
            # tx, ty = self.get_element(t).center()
            self.d.swipe(fx, fy, tx, ty, duration=0.1, steps=None)
        self.wait_a_second()
        self.click(self.done_button)
        self.wait_a_second()


