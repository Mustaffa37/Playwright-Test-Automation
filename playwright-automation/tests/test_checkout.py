import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)
        page.screenshot(path="screenshot.png")

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        cart_page.add_item_to_cart()
        cart_page.open_cart()
        checkout_page.proceed_to_checkout()
        checkout_page.enter_shipping_details("John", "Doe", "12345")
        checkout_page.complete_order()

        assert "checkout-complete" in page.url  # Verifying order completion
        browser.close()
