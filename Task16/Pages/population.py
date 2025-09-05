from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Population:
    def __init__(self,driver):
        self.driver=driver
        self.world_population_locator=(By.XPATH,"//div[@class='counter-ticker is-size-2-mobile']")

    def counting_population(self):
        wait=WebDriverWait(self.driver,10)
        count=wait.until(ec.visibility_of_element_located(self.world_population_locator))
        print(count.text)


