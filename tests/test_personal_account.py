from pages.personal_account_page import PersonalAccountPage
from data import Url
import allure


@allure.title('Тесты на личный кабинет')
class TestPersonalAccount:
    @allure.title('Проверка авторизации и перехода по клику на "Личный кабинет"')
    def test_check_transition_to_page_personal_account(self, authorization):
        authorization.get(Url.URL_HOME)
        page = PersonalAccountPage(authorization)
        page.go_to_personal_account()
        button = page.is_profile_visible()
        assert button.text == 'Профиль'

    @allure.title('Проверка авторизации и перехода в раздел "История заказов"')
    def test_check_transition_to_page_order_history(self, authorization):
        authorization.get(Url.URL_HOME)
        page = PersonalAccountPage(authorization)
        page.go_to_order_history()
        assert authorization.current_url == Url.URL_ORDER_HISTORY

    @allure.title('Проверка авторизации и выхода из аккаунта')
    def test_check_log_out_from_personal_account(self, authorization):
        authorization.get(Url.URL_HOME)
        page = PersonalAccountPage(authorization)
        page.log_out()
        assert authorization.current_url == Url.URL_ENTRANCE_PERSONAL_ACCOUNT
