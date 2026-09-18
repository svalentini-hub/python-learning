from playwright.sync_api import sync_playwright
from playwright.sync_api import expect




with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
#Login to the site
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_list")).to_be_visible()
    print("Login successful")
#add items to cart
   
    page.click("#add-to-cart-sauce-labs-backpack")

    #checking for the top-right icon
    expect(page.locator(".shopping_cart_link")).to_have_attribute("aria-label", "Cart, 1 items")
    print("You have 1 displayed over the cart icon")
    
    #checking for correct link
    page.click(".shopping_cart_container")
    page.wait_for_timeout(1000)
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    #checking for correct quantity
    expect(page.locator(".cart_quantity")).to_have_text("1")
    print("You have 1 item in the cart")

    #checking for correct item
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
    print("Correct item in the cart")
    browser.close()