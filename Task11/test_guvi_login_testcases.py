import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Run a automation script for scenario

# 1. visit to the url
# 2. login the url
# 3. login using valid credentials
# 4. close the browser

def test_scenario():
    try:
        option = Options()
        option.add_argument("--incognito")# Launches Chrome in Incognito mode
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
        driver.get("https://www.guvi.in/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.ID,"login-btn").click()
        driver.find_element(By.XPATH,"(//input[@class='form-control'])[1]").send_keys("")
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("")
        driver.find_element(By.XPATH, "//a[@class='btn login-btn']").click()
        time.sleep(5)
        driver.save_screenshot("Guvi_login.png")
        print(driver.title)
        print("Login successful")

    finally:
        driver.quit()

            # *******************postive test cases******************************

def testcase001_validate_login_url():
    try:
        option = Options()
        option.add_argument("--incognito")  # Launches Chrome in Incognito mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        driver.get("https://www.guvi.in/")
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(5)
        expected_url='https://www.guvi.in/sign-in/'
        actual_url=driver.current_url
        assert expected_url==actual_url,"Url is mismatching"

    finally:
        driver.quit()


def testcase002_validate_userfields():
    try:
        option = Options()
        option.add_argument("--incognito")  # Launches Chrome in Incognito mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        driver.get("https://www.guvi.in/")
        driver.find_element(By.ID, "login-btn").click()
        email_address=driver.find_element(By.XPATH, "(//input[@class='form-control'])[1]")
        password=driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]")
        if email_address.is_enabled() and email_address.is_displayed():
            print("yes email address is enabled")
        else:
            print("No email address field is disabled")
        if password.is_enabled() and password.is_displayed():
            print("yes password is enabled")
        else:
            print("No password field is disabled")

    finally:
        driver.quit()

def testcase003_validate_submit_button():
    try:
        option = Options()
        option.add_argument("--incognito")  # Launches Chrome in Incognito mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        driver.get("https://www.guvi.in/")
        driver.find_element(By.ID, "login-btn").click()
        login_button=driver.find_element(By.XPATH,"//a[@class='btn login-btn']")
        if login_button.is_enabled() and login_button.is_displayed():
            print("Login button enabled")

    finally:
        driver.quit()

                # ****************************Negative test cases*************************

def testcase004_validate_login_url():
    try:
        option = Options()
        option.add_argument("--incognito")  # Launches Chrome in Incognito mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        driver.get("https://www.guvi.in/")
        driver.find_element(By.ID, "login-btn").click()
        expected_url='https://www.guvi.in/sign-in/'
        actual_url=driver.current_url
        assert expected_url==actual_url, 'Url is mismatching'

    finally:
        driver.quit()


def testcase005_valid_email_Address_invalid_password():
    try:
        option = Options()
        option.add_argument("--incognito")# Launches Chrome in Incognito mode
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
        driver.get("https://www.guvi.in/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.ID,"login-btn").click()
        driver.find_element(By.XPATH,"(//input[@class='form-control'])[1]").send_keys("")
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Azar1509##")
        driver.find_element(By.XPATH, "//a[@class='btn login-btn']").click()
        invalid_credentials=driver.find_element(By.XPATH,"//div[@class='invalid-feedback is-invalid']").text
        print(invalid_credentials)


    finally:
        driver.quit()

def testcase006_invalid_email_Address_valid_password():
    try:
        option = Options()
        option.add_argument("--incognito")# Launches Chrome in Incognito mode
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
        driver.get("https://www.guvi.in/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.ID,"login-btn").click()
        driver.find_element(By.XPATH,"(//input[@class='form-control'])[1]").send_keys("sssy@gmail.com")
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys(" ")
        driver.find_element(By.XPATH, "//a[@class='btn login-btn']").click()
        invalid_credentials=driver.find_element(By.XPATH,"//div[@class='invalid-feedback is-invalid']").text
        print(invalid_credentials)


    finally:
        driver.quit()