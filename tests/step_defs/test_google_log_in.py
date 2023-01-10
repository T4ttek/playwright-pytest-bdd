from pytest_bdd import scenarios, scenario, given, when, then

from pages.base_page import BasePage
from pages.google_page import GooglePage


google_url = "https://www.google.com"
email = "meta.testtson"
password = "meta2022!"


@scenario('../features/google.feature', 'Log in to google account')
def test_log_in_to_google(page):
    pass


@given(u'User have open google website')
def open_website(page, env):
    # page.goto(google_url)
    env['base'].go_to_url(google_url)


@when(u'Click on the log in button')
def click_button(page, env):
    # google = GooglePage(page)
    env['google'].click_on_log_in_button()


@when(u'User set login field')
def login_field(page):
    google = GooglePage(page)
    google.set_email_field(email)


@when(u'User click on the next button')
def next_button(page):
    google = GooglePage(page)
    google.click_on_next_button()


@when(u'User set password field')
def password_field(page):
    google = GooglePage(page)
    google.set_password_field(password)


@then(u'User is logged in')
def logged_in(page):
    base = BasePage(page)
    base.waits(10)
