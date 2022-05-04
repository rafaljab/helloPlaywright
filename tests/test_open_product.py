from playwright.sync_api import expect

from pom.header import HeaderPage
from pom.home import HomePage
from pom.product import ProductPage
from pom.search import SearchPage


def test_open_best_seller_product_from_homepage(page):
    # Given
    home_page = HomePage(page)
    home_page.navigate()

    # When
    home_page.best_sellers_tab.click()
    first_element_title_str = home_page.best_seller_product_title(0).text_content()
    home_page.best_seller_product_title(0).click()

    # Then
    product_page = ProductPage(page)
    expect(product_page.product_title).to_have_text(first_element_title_str)


def test_open_product_from_search_results_list(page):
    # Given
    home_page = HomePage(page)
    home_page.navigate()

    # When
    header_page = HeaderPage(page)
    header_page.search("dress")

    page.wait_for_load_state("load")
    search_page = SearchPage(page)
    search_page.list_view_button.click()
    first_element_title_str = search_page.product_list_item_title(0).text_content()
    search_page.product_list_item_title(0).click()

    # Then
    product_page = ProductPage(page)
    expect(product_page.product_title).to_have_text(first_element_title_str)
