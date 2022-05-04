from playwright.sync_api import Locator


class HomePage:
    def __init__(self, page):
        self.page = page

        self.best_sellers_tab: Locator = page.locator("#home-page-tabs > li:nth-child(2) > a")
        self.best_sellers_products: Locator = page.locator("#blockbestsellers > li > div.product-container")

    def navigate(self):
        self.page.goto("http://www.automationpractice.com")

    def best_seller_product_title(self, number) -> Locator:
        return self.best_sellers_products.nth(number).locator("div.right-block > h5 > a")
