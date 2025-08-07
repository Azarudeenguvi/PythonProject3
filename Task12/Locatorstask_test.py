import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_open_guvi_url():
    try:
        options=Options()
        options.add_argument("--incognito")
        options.add_argument("start.maximized")
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.get("https://www.guvi.in/")
    finally:
        driver.quit()

def test_parent_element():
    try:
        options=Options()
        options.add_argument("--incognito")
        options.add_argument("start.maximized")
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.get("https://www.guvi.in/")

        # ***Parent-element***
        driver.find_element(By.XPATH,"//div[contains(@class,'⭐️rwl3jt-0 group')]/parent::div")

        #***First-child element***
        driver.find_element(By.XPATH,"//div[contains(@class,'⭐️rwl3jt-0 group')]/parent::div/child::a")
        # or
        driver.find_element(By.XPATH,"//div[contains(@class,'⭐️rwl3jt-0 hidden')]/child::a")

        #***Second-sibling***
        driver.find_element((By.XPATH,"//div[contains(@class,'⭐️rwl3jt-0 hidden')]/following-sibling::div"))

        #***parent_element_of_href***
        driver.find_element(By.XPATH,"(//a[@href='/courses/']/parent::div)[1]")

        #***ancestor***
        driver.find_element(By.XPATH,"//a[@href='/courses/']/ancestor::*")

        #***all following elements***
        driver.find_element(By.XPATH,"(//a[@href='/courses/'])[1]/following-sibling::div")

        #***all preceding elements***
        driver.find_element(By.XPATH,"((//a[@href='/courses/'])[1]/following-sibling::div)[4]/preceding-sibling::div")

    finally:

        driver.quit()



