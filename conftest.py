import pytest
from selenium import webdriver
import data
from data import Url, UserData
from pages.base_page import BasePage
from locators import PersonalAccountLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def ChromeOptions():
    pass


def FirefoxOptions():
    pass


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        data.DRIVER_NAME = 'chrome'
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    else:
        data.DRIVER_NAME = 'firefox'
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def authorization(driver):
    page = BasePage(driver)
    driver.get(Url.URL_ENTRANCE_PERSONAL_ACCOUNT)
    page.add_text_to_element(PersonalAccountLocators.FIELD_EMAIL, UserData.email)
    page.add_text_to_element(PersonalAccountLocators.FIELD_PASSWORD, UserData.password)
    page.click_element(PersonalAccountLocators.BUTTON_LOG_IN)
    WebDriverWait(driver, 10).until((EC.url_to_be(Url.URL_HOME)))
    yield driver
