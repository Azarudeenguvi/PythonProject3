from argparse import Action
from itertools import dropwhile

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.test_saucedemo
def test_saucedemo_webpage_contents():
    try:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID,"user-name").send_keys('standard_user')
        driver.find_element(By.ID,'password').send_keys('secret_sauce')
        driver.find_element(By.ID,'login-button').click()
        pagetitle=driver.title
        current_URL=driver.current_url
        allemelments=driver.find_element(By.TAG_NAME,'body').text
        with open('Webpage_task_10.txt','w')as file:
            file.write(allemelments)
        # This print the webpage title
        print(pagetitle)

        # This print the current URL of the webpage
        print(current_URL)

    finally:
        driver.quit()

@pytest.mark.title_webapplication
def testcase_001_title_web_application():
    try:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        assert "Swag Labs" in driver.title

    finally:
        driver.quit()

@pytest.mark.title_homepage
def testcase_002_url_of_homepage():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        assert "saucedemo.com" in driver.current_url

    finally:
        driver.quit()


@pytest.mark.login_postive_case
def testcase_003_login_positive_case():
    # go to the provided website and print the 'title of application' and 'url of the homepage'

    try:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        Get_title=driver.title
        # valid login details
        driver.find_element(By.ID, "user-name").send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        # logged in then validate the page using assertion
        expected_text='Products'
        Actual_text=driver.find_element(By.XPATH,"//span[text()='Products']").text
        assert expected_text==Actual_text
        print("Login successful")

        Get_url = driver.current_url

        print(Get_url)
        print(Get_title)
    finally:
        driver.quit()

@pytest.mark.negativecase_1
def testcase_004_negative_cases1():
    # go to the provided website and try login with invalid username and valid password

    try:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        Get_title=driver.title
        # valid login details
        driver.find_element(By.ID, "user-name").send_keys('standard_user123')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        expected_status='Epic sadface: Username and password do not match any user in this service'
        Actual_status=driver.find_element(By.XPATH,"//div[@class='error-message-container error']").text
        print(Actual_status)
        assert expected_status==Actual_status
        print("Login unsuccessful")

    finally:
        driver.quit()


@pytest.mark.negativecase_2
def testcase_005_negative_cases2():
    # go to the provided website and try login with valid username and invalid password

    try:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        Get_title=driver.title
        # valid login details
        driver.find_element(By.ID, "user-name").send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('demo123')
        driver.find_element(By.ID, 'login-button').click()
        expected_status='Epic sadface: Username and password do not match any user in this service'
        Actual_status=driver.find_element(By.XPATH,"//div[@class='error-message-container error']").text
        print(Actual_status)
        assert expected_status==Actual_status
        print("Login unsuccessful")

    finally:
        driver.quit()