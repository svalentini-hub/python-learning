from playwright.sync_api import expect


#pytest-playwright uses chromium.launch() + new_page() as default
def test_add_item_to_cart(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_list")).to_be_visible()

    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, 1 items")

    page.click(".shopping_cart_container")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
    expect(page.locator(".cart_quantity")).to_have_text("1")