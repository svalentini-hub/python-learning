import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="function")
def logged_in_page(page):
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_list")).to_be_visible()
    return page