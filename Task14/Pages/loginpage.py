from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginDetails:
    def __init__(self,driver):
        self.driver=driver
        self.email_locator=(By.XPATH,'//input[@placeholder="Enter your mail"]')
        self.password_locator=(By.XPATH,'//input[@placeholder="Enter your password "]')
        self.signin_locator=(By.XPATH,'//button[@type="submit"]')
        self.forget_password_locator=(By.ID,':r1:-helper-text')
        self.invalid_email_locator=(By.XPATH,'//p[text()="*Incorrect email!"]')
        self.login_text_locator=(By.XPATH,'//div[contains(@class,"login-text ")]')

    def email(self,email):
        wait = WebDriverWait(self.driver, 10)
        email_input= wait.until(ec.visibility_of_element_located(self.email_locator))
        email_input.send_keys(email)

    def password(self,password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def signin_button(self):
        self.driver.find_element(*self.signin_locator).click()

    def assert_invalid_email(self):
        wait=WebDriverWait(self.driver,10)
        pass_text=wait.until(ec.visibility_of_element_located(self.invalid_email_locator))
        actual_text=pass_text.text
        expected_text='*Incorrect email!'
        assert actual_text==expected_text,'logged in successfully'


    def assert_invalid_pass(self):
        wait=WebDriverWait(self.driver,10)
        pass_text=wait.until(ec.visibility_of_element_located(self.forget_password_locator))
        actual_text=pass_text.text
        expected_text='Incorrect password!'
        assert actual_text==expected_text,'logged in successfully'

    def email_is_enabled(self):
        return self.driver.find_element(*self.email_locator).is_enabled()

    def password_is_enabled(self):
        return self.driver.find_element(*self.password_locator).is_enabled()

    def signin_button_is_enabled(self):
        return self.driver.find_element(*self.signin_locator).is_enabled()

    def login_text(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(ec.visibility_of_element_located(self.login_text_locator))