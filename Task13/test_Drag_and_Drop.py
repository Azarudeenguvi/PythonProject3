from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def test_drag_drop():

    try:
        options=Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        driver.get("https://jqueryui.com/droppable/")
        # Switch to iframe
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        drag=driver.find_element(By.XPATH,'//div[contains(@class,"ui-widget-content ui-draggable")]')
        drop=driver.find_element(By.XPATH,'//div[contains(@class,"ui-widget-header ui-droppable")]')
        actions=ActionChains(driver)
        actions.drag_and_drop(source=drag,target=drop).perform()
        driver.save_screenshot("drag_drop.png")


    finally:
        driver.quit()

def test_negative_case():
    try:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://jqueryui.com/droppable/")
        # Switch to iframe
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        drag = driver.find_element(By.XPATH, '//div[contains(@class,"ui-widget-content ui-draggable")]')
        drop = driver.find_element(By.XPATH, '//div[contains(@class,"ui-widget-header ui-droppable")]')
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(source=drag,xoffset=342,yoffset=140).perform()
        driver.save_screenshot("outside_drop.png")
        drop_here=driver.find_element(By.XPATH,"//div[@id='droppable']/p").text
        expected_text='Drop here'
        print(f"Drop zone text after invalid drop: {drop_here}")
        assert drop_here==expected_text, "Drop zone text changed unexpectedly"
        driver.save_screenshot("outside_drop.png")

    finally:
        driver.quit()



