import pytest

# @pytest.fixture
# def driver():
#     print("\n[Setup] Open Browser")
#     driver = "ChromeDriver"
#     yield driver
#     print("[Teardown] Close Browser")
#
# def test_title(driver):
#     print(f"Running test with {driver}")
#     assert driver == "ChromeDriver"

import pytest

@pytest.fixture
def login():
    print("\n[Setup] Login as user")
    yield "azarsece@gmail.com"
    print("[Teardown] Logout user")

def test_valid_login(login):
    print(f"Testing with valid login: {login}")
    assert login == "azarsece@gmail.com"

def test_dashboard_access(login):
    print(f"Checking dashboard for {login}")
    assert "@" in login