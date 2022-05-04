from playwright.sync_api import Locator


class ProductPage:
    def __init__(self, page):
        self.page = page

        self.product_title: Locator = page.locator("#center_column > div > div > div.pb-center-column.col-xs-12.col-sm-4 > h1")
