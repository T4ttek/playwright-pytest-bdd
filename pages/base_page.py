from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_url(self, url):
        self.page.goto(url)

    def click_on_element(self, selector):
        return self.page.click(selector)

    def type_in_element(self, selector, text):
        return self.page.type(selector, text)

    def waits(self, time):
        seconds = time*1000
        return self.page.wait_for_timeout(seconds)
