from pages.base_page import BasePage
from locators import PersonalAccountLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


# Личный кабинет
class PersonalAccountPage(BasePage):
    @allure.step('Перейти в личный кабинет')
    def go_to_personal_account(self):
        self.click_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Перейти в историю заказов')
    def go_to_order_history(self):
        self.go_to_personal_account()
        self.click_element(PersonalAccountLocators.BUTTON_HISTORY_ORDERS)

    @allure.step('Выйти из личного кабинета')
    def log_out(self):
        self.go_to_personal_account()
        self.click_element(PersonalAccountLocators.BUTTON_LOGOUT)
        WebDriverWait(self.driver, self.time).until(EC.invisibility_of_element_located(PersonalAccountLocators.BUTTON_LOGOUT))

    @allure.step('Дождаться загрузки кнопки "Профиль"')
    def is_profile_visible(self):
        return WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(PersonalAccountLocators.BUTTON_PROFILE))
