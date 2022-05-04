from playwright.sync_api import Locator


class SearchPage:
    def __init__(self, page):
        self.page = page

        self.list_view_button: Locator = page.locator("#list i")
        self.grid_view_button: Locator = page.locator("#grid > a > i")

        self.product_list_items: Locator = page.locator("#center_column > ul > li")

    def product_list_item_title(self, number) -> Locator:
        return self.product_list_items.nth(number).locator("div > div > div > h5 > a")
