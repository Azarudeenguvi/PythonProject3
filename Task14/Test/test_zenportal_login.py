
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

from Task14.Pages.Dashboard import DashboardDetails
from Task14.Pages.loginpage import LoginDetails

@pytest.mark.testcase1
def test_successful_login():
    try:
        options=Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.get('https://www.zenclass.in/login')
        log1=LoginDetails(driver)
        log1.email('azarsece@gmail.com')
        log1.password('Azar1509#')
        log1.signin_button()
        das=DashboardDetails(driver)
        assert das.dashboard_validate(),"Dashboard text is not displayed"

    finally:
        driver.quit()


@pytest.mark.testcase2
def test_unsuccessful_login_invalid_email():
    try:
        options=Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.get('https://www.zenclass.in/login')
        log1=LoginDetails(driver)
        log1.email('Ttest151@gmail.com')
        log1.password('Azar1509#')
        log1.signin_button()
        log1.assert_invalid_email()

    finally:
        driver.quit()

@pytest.mark.testcase3
def test_unsuccessful_login_invalid_password():
    try:
        options=Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.get('https://www.zenclass.in/login')
        log1=LoginDetails(driver)
        log1.email('azarsece@gmail.com')
        log1.password('Azar15099#')
        log1.signin_button()
        log1.assert_invalid_pass()

    finally:
        driver.quit()

@pytest.mark.testcase4
def test_validate_username_password_input_box():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get('https://www.zenclass.in/login')
        log1 = LoginDetails(driver)
        assert log1.email_is_enabled()
        assert log1.password_is_enabled()

    finally:
        driver.quit()



@pytest.mark.testcase5
def test_validate_submit_button():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get('https://www.zenclass.in/login')
        log1 = LoginDetails(driver)
        assert log1.signin_button_is_enabled()
    finally:
        driver.quit()


@pytest.mark.testcase6
def test_logout_functionality():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get('https://www.zenclass.in/login')
        log1 = LoginDetails(driver)
        log1.email('azarsece@gmail.com')
        log1.password('Azar1509#')
        log1.signin_button()
        das=DashboardDetails(driver)
        das.close_modal()
        das.dashboard_validate()
        das.profile_click()
        assert das.logout_enabled(),'Logout not enabled'
        das.logout_click()
        log1.login_text()


    finally:
        driver.quit()

