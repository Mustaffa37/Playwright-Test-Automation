from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = "text=Add to cart"
        self.cart_icon = ".shopping_cart_link"

    def add_item_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def open_cart(self):
        self.page.click(self.cart_icon)
