import pytest
import allure
import data
from data import Url
from pages.main_functionality_page import MainFunctionalityPage
from locators import ConstructorLocators


@allure.title('Тесты на проверку основного функционала')
class TestMainFunctionality:
    @allure.title('Проверка перехода на "Конструктор" из формы авторизации')
    def test_check_go_to_constructor_from_personal_account_unauthorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        page = MainFunctionalityPage(driver)
        page.go_to_personal_account_unauthorized()
        page.go_to_constructor()
        text = page.is_constrictor_visible().text
        assert text == 'Соберите бургер'

    #
    @allure.title('Проверка перехода на "Конструктор" из Личного кабинета')
    def test_check_go_to_constructor_from_personal_account_authorized(self, authorization):
        authorization.get(Url.URL_HOME)
        page = MainFunctionalityPage(authorization)
        page.go_to_personal_account_authorized()
        page.go_to_constructor()
        text = page.is_constrictor_visible().text
        assert text == 'Соберите бургер'

    @allure.title('Проверка перехода на "Конструктор" из "Ленты заказов"')
    def test_check_go_to_constructor_from_order_feed(self, driver):
        driver.get(Url.URL_ORDER_FEED)
        page = MainFunctionalityPage(driver)
        page.go_to_constructor()
        text = page.is_constrictor_visible().text
        assert text == 'Соберите бургер'

    @allure.title('Проверка перехода на "Ленту заказов" из формы авторизации')
    def test_check_go_to_order_feed_from_personal_account_unauthorized(self, driver):
        driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
        page = MainFunctionalityPage(driver)
        page.go_to_personal_account_unauthorized()
        page.go_to_order_feed()
        text = page.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @allure.title('Проверка перехода на "Ленту заказов" из Личного кабинета')
    def test_check_go_to_order_feed_from_personal_account_authorized(self, authorization):
        authorization.get(Url.URL_HOME)
        page = MainFunctionalityPage(authorization)
        page.go_to_personal_account_authorized()
        page.go_to_order_feed()
        text = page.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @allure.title('Проверка перехода на "Ленту заказов" из Конструктора')
    def test_check_go_to_order_feed_from_constructor(self, driver):
        driver.get(Url.URL_HOME)
        page = MainFunctionalityPage(driver)
        page.go_to_order_feed()
        text = page.is_order_feed_visible().text
        assert text == 'Лента заказов'

    @pytest.mark.parametrize("index", range(1, 16))
    @allure.title('Проверка открытия всплывающего окна с деталями ингредиента и закрытия этого окна')
    def test_check_ingredient_details_go_to_ingredient(self, driver, index):
        driver.get(Url.URL_HOME)
        page = MainFunctionalityPage(driver)
        page.go_to_ingredient_by_index(index)
        page.close_ingredient_details()
        text = page.is_ingredient_details_visible().text
        assert text == 'Детали ингредиента'

    @pytest.mark.parametrize("index", range(1, 16))
    @allure.title('Проверка увеличения каунтера ингредиента при добавлении данного ингредиента в заказ')
    def test_drag_and_drop_ingredient_with_counter(self, driver, index):
        driver.get(Url.URL_HOME)
        page = MainFunctionalityPage(driver)
        if data.DRIVER_NAME == 'chrome':
            page.drag_and_drop_ingredient(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        else:
            page.drag_and_drop_ingredient_firefox(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        counter = page.get_counter_value(index)
        assert counter > 0

    @pytest.mark.parametrize("ingredients", [[1], [2, 5], [1, 4, 14]])
    @allure.title('Проверка успешного оформления заказа с разными наборами ингредиентов авторизованным пользователем')
    def test_place_order_with_multiple_ingredients(self, authorization, ingredients):
        authorization.get(Url.URL_HOME)
        page = MainFunctionalityPage(authorization)
        for index in ingredients:
            if data.DRIVER_NAME == 'chrome':
                page.drag_and_drop_ingredient(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
            else:
                page.drag_and_drop_ingredient_firefox(index, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        page.click_button_place_order()
        text = page.is_window_order_id_visible().text
        assert text == 'идентификатор заказа'
