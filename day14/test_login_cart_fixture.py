import pytest
from playwright.sync_api import expect


@pytest.fixture
def logged_in_page(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_list")).to_be_visible()
    return page

def test_add_item_to_cart(logged_in_page):
    logged_in_page.click("#add-to-cart-sauce-labs-backpack")
    expect(logged_in_page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, 1 items")
    logged_in_page.click(".shopping_cart_container")
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(logged_in_page.locator(".cart_item .inventory_item_name")).to_have_text("Sauce Labs Backpack")
    expect(logged_in_page.locator(".cart_quantity")).to_have_text("1")

def test_remove_item_from_cart(logged_in_page):
    logged_in_page.click("#add-to-cart-sauce-labs-backpack")
    expect(logged_in_page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, 1 items")

    logged_in_page.click(".shopping_cart_container")
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")

    logged_in_page.click("#remove-sauce-labs-backpack")
    expect(logged_in_page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, empty")