class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_backpack_to_cart(self):
        self.page.click("#add-to-cart-sauce-labs-backpack")

    def go_to_cart(self):
        self.page.click(".shopping_cart_container")

    def cart_link_locator(self):
        return self.page.locator(".shopping_cart_link")