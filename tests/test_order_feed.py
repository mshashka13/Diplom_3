import allure
from data import Url
from pages.order_feed_page import OrderFeedPage


@allure.title('Тесты на проверку раздела "Лента заказов"')
class TestOrderFeed:
    @allure.title('Проверка всплывающего окна с деталями заказа при клике на заказ')
    def test_check_window_with_order_details(self, driver):
        driver.get(Url.URL_ORDER_FEED)
        page = OrderFeedPage(driver)
        page.click_to_first_order_from_order_feed()
        element = page.is_window_with_order_details_visible()
        assert element is not None

    @allure.title('Проверка отображения заказов из "Истории заказов" пользователя в "Ленте заказов"')
    def test_check_show_orders_from_orders_history_on_order_feed(self, authorization):
        authorization.get(Url.URL_HOME)
        page = OrderFeedPage(authorization)
        page.go_to_personal_account()
        page.go_to_order_history()
        order_id = page.get_order_id_from_order_history()
        page.go_to_order_feed()
        element = page.order_by_id(order_id)
        assert element is not None

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа')
    def test_check_increment_counter_completed_for_all_time_when_creating_order(self, authorization, driver):
        authorization.get(Url.URL_ORDER_FEED)
        page = OrderFeedPage(authorization)
        counter_before_order = page.get_text_from_counter_completed_for_all_time()
        page.go_to_constructor()
        page.create_order(driver)
        page.close_window_order_id()
        page.go_to_order_feed()
        counter_after_order = page.get_text_from_counter_completed_for_all_time()
        assert counter_after_order > counter_before_order

    #
    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_check_increment_counter_completed_for_today_when_creating_order(self, authorization, driver):
        authorization.get(Url.URL_ORDER_FEED)
        page = OrderFeedPage(authorization)
        counter_before_order = page.get_text_from_counter_completed_for_today()
        page.go_to_constructor()
        page.create_order(driver)
        page.close_window_order_id()
        page.go_to_order_feed()
        counter_after_order = page.get_text_from_counter_completed_for_today()
        assert counter_after_order > counter_before_order

    #
    @allure.title('Проверка появления заказа в разделе "В работе" после его оформления')
    def test_check_show_order_in_work_when_creating_order(self, authorization, driver):
        authorization.get(Url.URL_HOME)
        page = OrderFeedPage(authorization)
        page.create_order(driver)
        order_id = page.wait_for_id_to_change()
        page.close_window_order_id()
        page.go_to_order_feed()
        order_id_in_work = page.wait_for_text_in_work_to_change()
        assert order_id == order_id_in_work
