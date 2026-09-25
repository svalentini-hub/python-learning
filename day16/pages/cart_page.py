class CartPage:
    def __init__(self, page):
        self.page = page

    def remove_backpack(self):
        self.page.click("#remove-sauce-labs-backpack")

    # a locator, not an assertion, the test decides what to check

    def item_name_locator(self):
        return self.page.locator(".cart_item .inventory_item_name")

    def cart_link_locator(self):
        return self.page.locator(".shopping_cart_link")
    