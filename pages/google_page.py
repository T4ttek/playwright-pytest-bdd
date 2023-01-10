from playwright.sync_api import Page

from pages.base_page import BasePage


class GooglePage(BasePage):

    email_field = "//input[@type='email']"
    log_in_button = "div~button"
    next_button = "div>div>div>div>div:nth-of-type(1)>div>div>button>span"
    password_field = "input[type='password']"

    def click_on_log_in_button(self):
        return self.click_on_element(self.log_in_button)
        # return self.page.click(self.log_in_button)

    def set_email_field(self, email):
        return self.page.type(self.email_field, email)

    def click_on_next_button(self):
        return self.page.click(self.next_button)

    def click_on_password_field(self):
        return self.page.click(self.password_field)

    def set_password_field(self, password):
        self.click_on_password_field()
        return self.page.type(self.password_field, password)
