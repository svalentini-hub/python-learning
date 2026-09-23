from playwright.sync_api import expect
#separate function in case of 20 tests, so we only need to edit the login function here
def login(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


#pytest-playwright uses chromium.launch() + new_page() as default
def test_add_item_to_cart(page):
    login(page)
    expect(page.locator(".inventory_list")).to_be_visible()

    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, 1 items")

    page.click(".shopping_cart_container")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.locator(".cart_item .inventory_item_name")).to_have_text("Sauce Labs Backpack")
    expect(page.locator(".cart_quantity")).to_have_text("1")



def test_remove_item_from_cart(page):
    login(page)
    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, 1 items")

    page.click(".shopping_cart_container")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    # now remove it — inspect the cart page yourself to find this button's selector
    page.click("#remove-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, empty")