from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators import PersonalAccountLocators, ConstructorLocators, OrderFeedLocators
from selenium.webdriver import ActionChains
import allure
import data


# Лента заказов
class OrderFeedPage(BasePage):

    @allure.step('Перейти в личный кабинет')
    def go_to_personal_account(self):
        self.click_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Перейти в историю заказов')
    def go_to_order_history(self):
        self.go_to_personal_account()
        self.click_element(PersonalAccountLocators.BUTTON_HISTORY_ORDERS)

    @allure.step('Перейти в конструктор')
    def go_to_constructor(self):
        self.click_element(ConstructorLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Получить номер последнего заказа в "Истории заказов"')
    def get_order_id_from_order_history(self):
        order = self.find_element_webdriverwait(PersonalAccountLocators.LAST_ORDER_FROM_ORDER_HISTORY)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order)
        return self.get_text_from_element(PersonalAccountLocators.LAST_ORDER_FROM_ORDER_HISTORY)

    @allure.step('Клик на первый заказ в списке "Ленты заказов"')
    def click_to_first_order_from_order_feed(self):
        self.click_element(OrderFeedLocators.ORDER_FROM_ORDER_FEED)

    @allure.step('Дождаться загрузки текста в окне "Детали заказа"')
    def is_window_with_order_details_visible(self):
        return WebDriverWait(self.driver, self.time).until(
            EC.visibility_of_element_located(OrderFeedLocators.TEXT_COMPOSITION_ORDER))

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
        return WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(ConstructorLocators.TEXT_INGREDIENT_DETAILS))

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

    @allure.step('Оформить заказ')
    def create_order(self, driver):
        page = OrderFeedPage(driver)
        if data.DRIVER_NAME == 'chrome':
            page.drag_and_drop_ingredient(2, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        else:
            page.drag_and_drop_ingredient_firefox(2, ConstructorLocators.DROP_ZONE_CONSTRUCTOR)
        page.click_button_place_order()

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_button_place_order(self):
        self.click_element(ConstructorLocators.BUTTON_PLACE_ORDER)

    @allure.step('Дождаться изменения текста идентификатора заказа')
    def wait_for_id_to_change(self):
        wait = WebDriverWait(self.driver, self.time)
        while True:
            new_value = self.get_text_from_element(OrderFeedLocators.TEXT_ORDER_ID)
            if new_value and new_value != "9999":
                return new_value

    @allure.step('Закрыть окно с id заказа')
    def close_window_order_id(self):
        self.click_element(OrderFeedLocators.BUTTON_CLOSE_ORDER_ID)

    @allure.step('Перейти в "Ленту заказов"')
    def go_to_order_feed(self):
        self.click_element(OrderFeedLocators.BUTTON_ORDER_FEED)

    # Динамический локатор заказа по его id в Ленте заказов
    @staticmethod
    def order_by_id(order_id):
        return By.XPATH, f".//p[contains(@class, 'text text_type_digits-default') and contains(text(), '{order_id}')]"

    @allure.step('Получить значение счетчика "Выполнено за все время"')
    def get_text_from_counter_completed_for_all_time(self):
        return self.get_text_from_element(OrderFeedLocators.TEXT_COUNTER_COMPLETED_FOR_ALL_TIME)

    @allure.step('Получить значение счетчика "Выполнено за сегодня"')
    def get_text_from_counter_completed_for_today(self):
        return self.get_text_from_element(OrderFeedLocators.TEXT_COUNTER_COMPLETED_FOR_TODAY)

    @allure.step('Дождаться изменения текста в разделе "В работе"')
    def wait_for_text_in_work_to_change(self):
        wait = WebDriverWait(self.driver, self.time)
        while True:
            new_value = self.get_text_from_element(OrderFeedLocators.TEXT_ORDER_ID)
            if new_value and new_value != "9999":
                return new_value
