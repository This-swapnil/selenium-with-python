from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 30)

driver.implicitly_wait(30)

driver.get("https://www.bing.com/")

searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()

searchlink = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h2[@class=' b_topTitle']//a[normalize-space()='Selenium']")
    )
)

searchlink.click()


sleep(2)
driver.quit()
