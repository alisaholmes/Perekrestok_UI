import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = "https://www.perekrestok.ru/"
    browser.config.timeout = 10.0
    browser.config.window_height = 1366
    browser.config.window_width = 1024

    yield
    browser.quit()