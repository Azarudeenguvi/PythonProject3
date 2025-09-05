import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    print("\n[Setup] Launch Browser")
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver  # test runs here

    print("[Teardown] Quit Browser")
    driver.quit()