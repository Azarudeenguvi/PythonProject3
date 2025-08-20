from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DashboardDetails:
    def __init__(self,driver):
        self.driver=driver
        self.dashboard_locator=(By.XPATH,'//div[contains(@class,"info-btn-")]/child::p')
        self.profile_name_locator=(By.XPATH,'//div[@class="user-name-div"]')
        self.logout_locator=(By.XPATH,'//div[text()="Log out"]')
        self.close_modal_locator=(By.XPATH,'//button[@class="custom-close-button"]')



    def dashboard_validate(self):
        wait = WebDriverWait(self.driver, 10)
        dashboard_text=wait.until(ec.visibility_of_element_located(self.dashboard_locator))
        actual_text=dashboard_text.text
        expected_text='Dashboard'
        return actual_text==expected_text

    def profile_click(self):
        self.driver.find_element(*self.profile_name_locator).click()

    def logout_enabled(self):
        return self.driver.find_element(*self.logout_locator).is_enabled()

    def logout_click(self):
        self.driver.find_element(*self.logout_locator).click()

    def close_modal(self):
            try:
                wait = WebDriverWait(self.driver, 10)
                close_modal1 = wait.until(ec.element_to_be_clickable(self.close_modal_locator))
                close_modal1.click()
            except(TimeoutException, NoSuchElementException):
                pass




