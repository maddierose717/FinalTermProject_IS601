import pytest
from playwright.sync_api import Page, expect

def test_profile_page_redirects_if_not_logged_in(page: Page):
    """Test that profile page redirects to login if not authenticated"""
    page.goto("http://localhost:8000/profile")
    # Should redirect to login since no token
    page.wait_for_url("**/login")
    
def test_user_can_view_profile_after_login(page: Page):
    """Test complete flow: register -> login -> view profile"""
    # Register a new user
    page.goto("http://localhost:8000/register")
    
    import random
    rand = random.randint(1000, 9999)
    username = f"testuser{rand}"
    email = f"test{rand}@example.com"
    
    page.fill('input[name="username"]', username)
    page.fill('input[name="email"]', email)
    page.fill('input[name="first_name"]', "Test")
    page.fill('input[name="last_name"]', "User")
    page.fill('input[name="password"]', "TestPass123!")
    page.fill('input[name="confirm_password"]', "TestPass123!")
    page.click('button[type="submit"]')
    
    # Wait a bit for registration
    page.wait_for_timeout(1000)
    
    # Login
    page.goto("http://localhost:8000/login")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', "TestPass123!")
    page.click('button[type="submit"]')
    
    # Wait for redirect to dashboard
    page.wait_for_url("**/dashboard", timeout=5000)
    
    # Go to profile
    page.goto("http://localhost:8000/profile")
    
    # Check profile info is displayed
    expect(page.locator('#show_username')).to_have_text(username)
    expect(page.locator('#show_email')).to_have_text(email)
