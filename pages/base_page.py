from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Базовые методы
class BasePage:
    def __init__(self, driver, time=10):
        self.driver = driver
        self.time = time

    # Найти элемент
    def find_element_webdriverwait(self, locator):
        WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Кликнуть элемент
    def click_element(self, locator):
        element = WebDriverWait(self.driver, self.time).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    # Ввести текст в элементе
    def add_text_to_element(self, locator, text):
        WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    # Получить текст элемента
    def get_text_from_element(self, locator):
        text = WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator)).text
        return text

    # Скроллить до элемента
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    # Дождаться когда поменяется URL
    def url_changes(self, original_url):
        WebDriverWait(self.driver, self.time).until(EC.url_changes(original_url))

    # Получить новый URL
    def wait_for_url_change(self, original_url):
        WebDriverWait(self.driver, self.time).until(EC.url_changes(original_url))
        return self.driver.current_url