from playwright.sync_api import sync_playwright

import pytest

from pages.base_page import BasePage
from pages.google_page import GooglePage


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        page = browser.new_page(geolocation={"longitude": -76.12713, "latitude": 43.034706})
        yield page
        browser.close()


@pytest.fixture
def env(page):
    base = BasePage(page)
    google = GooglePage(page)
    pages = {
        'base': base,
        'google': google,
    }
    return pages

#
# class Environment:
#     def __init__(self, page):
#         self.base = BasePage(page)
#         self.google = GooglePage(page)
