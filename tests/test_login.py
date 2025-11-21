import pytest
from pages.login_page import LoginPage

def test_standard_user_login(page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    
    login_page.login("standard_user", "secret_sauce")
    
    assert "inventory.html" in page.url
    assert page.locator(".title").inner_text() == "Products"