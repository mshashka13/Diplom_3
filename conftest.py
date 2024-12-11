import pytest
from selenium import webdriver
import data
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        data.DRIVER_NAME = 'chrome'
        driver = webdriver.Chrome()
    else:
        data.DRIVER_NAME = 'firefox'
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def personal_account(driver):
    return PersonalAccountPage(driver)


@pytest.fixture
def constructor(driver):
    return ConstructorPage(driver)


@pytest.fixture
def order_feed(driver):
    return OrderFeedPage(driver)
