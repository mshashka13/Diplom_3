from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators import PersonalAccountLocators, ConstructorLocators, OrderFeedLocators
from selenium.webdriver import ActionChains
import allure


# Основной функционал
class MainFunctionalityPage(BasePage):
    @allure.step('Перейти в "Личный кабинет" без авторизации')
    def go_to_personal_account_unauthorized(self):
        self.click_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, self.time).until(
            EC.visibility_of_element_located(PersonalAccountLocators.FIELD_EMAIL))

    @allure.step('Перейти в "Личный кабинет" с авторизацией')
    def go_to_personal_account_authorized(self):
        self.click_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(PersonalAccountLocators.BUTTON_PROFILE))

    @allure.step('Перейти в "Конструктор"')
    def go_to_constructor(self):
        self.click_element(ConstructorLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Перейти в "Ленту заказов"')
    def go_to_order_feed(self):
        self.click_element(OrderFeedLocators.BUTTON_ORDER_FEED)

    @allure.step('Дождаться загрузки заглавного текста в "Конструкторе"')
    def is_constrictor_visible(self):
        return WebDriverWait(self.driver, self.time).until(
            EC.visibility_of_element_located(ConstructorLocators.TEXT_COLLECT_BURGER))

    @allure.step('Дождаться загрузки заглавного текста в "Ленте заказов"')
    def is_order_feed_visible(self):
        return WebDriverWait(self.driver, self.time).until(
            EC.visibility_of_element_located(OrderFeedLocators.TEXT_ORDER_FEED))

    # Динамический локатор ингредиента по индексу
    @staticmethod
    def burger_ingredient_by_index(index):
        return By.XPATH, f"(.//*[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'])[{index}]"

    @allure.step('Открыть "Детали ингредиента" по индексу ингредиента')
    def go_to_ingredient_by_index(self, index):
        locator = self.burger_ingredient_by_index(index)
        self.click_element(locator)

    @allure.step('Дождаться загрузки текста в окне "Детали ингредиента"')
    def is_ingredient_details_visible(self):
        return WebDriverWait(self.driver, self.time).until(
            EC.visibility_of_element_located(ConstructorLocators.TEXT_INGREDIENT_DETAILS))

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_ingredient_details(self):
        self.click_element(ConstructorLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)

    @allure.step('Скроллить до ингредиента')
    def scroll_to_ingredient(self, index):
        ingredient = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ingredient)

    @allure.step('Перетащить ингредиент по индексу в зону конструктора')
    def drag_and_drop_ingredient(self, index, drop_zone_locator):
        self.scroll_to_ingredient(index)
        ingredient = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        drop_zone = self.find_element_webdriverwait(drop_zone_locator)
        ActionChains(self.driver).drag_and_drop(ingredient, drop_zone).perform()

    # Динамический локатор каунтера по индексу
    @staticmethod
    def get_ingredient_by_counter(index):
        return By.XPATH, f"(.//p[@class='counter_counter__num__3nue1'])[{index}]"

    @allure.step('Получить значение каунтера ингредиента по индексу')
    def get_counter_value(self, index):
        counter_locator = self.get_ingredient_by_counter(index)
        counter_element = WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(counter_locator))
        return int(counter_element.text)

    @allure.step('Перетащить ингредиент по индексу в зону конструктора в бразуере Firefox')
    def drag_and_drop_ingredient_firefox(self, index, locator_to):
        element_from = self.find_element_webdriverwait(self.burger_ingredient_by_index(index))
        element_to = self.find_element_webdriverwait(locator_to)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            """, element_from, element_to)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_button_place_order(self):
        self.click_element(ConstructorLocators.BUTTON_PLACE_ORDER)

    @allure.step('Дождаться появления окна с идентификатором заказа')
    def is_window_order_id_visible(self):
        return WebDriverWait(self.driver, self.time).until(
            EC.visibility_of_element_located(ConstructorLocators.TEXT_ORDER_ID))
