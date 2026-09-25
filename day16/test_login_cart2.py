import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_item_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(logged_in_page.locator(".cart_item .inventory_item_name")).to_have_text("Sauce Labs Backpack")
    expect(logged_in_page.locator(".cart_quantity")).to_have_text("1")

def test_remove_item_from_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    expect(logged_in_page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, 1 items")

    cart_page = CartPage(logged_in_page)
    cart_page.remove_backpack()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(logged_in_page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, empty")