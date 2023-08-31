import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://github.com'
    browser_option = webdriver.ChromeOptions()
    browser_option.add_argument('--headless')
    browser_option.add_argument('window-size=1920,1080')
    browser.config.driver_options = browser_option

    yield

    browser.quit()