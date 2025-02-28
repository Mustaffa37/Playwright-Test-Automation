import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        cart_page = CartPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        cart_page.add_item_to_cart()
        cart_page.open_cart()

        assert "cart" in page.url  # Verifying cart page is opened
        browser.close()