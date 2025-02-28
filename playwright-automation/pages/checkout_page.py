from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = "#checkout"
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)

    def enter_shipping_details(self, first, last, zip_code):
        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.postal_code, zip_code)
        self.page.click(self.continue_button)

    def complete_order(self):
        self.page.click(self.finish_button)
