from playwright.sync_api import Locator


class HeaderPage:
    def __init__(self, page):
        self.page = page

        self.search_field: Locator = page.locator("[placeholder=\"Search\"]")

    def search(self, text):
        self.search_field.fill(text)
        self.search_field.press("Enter")
