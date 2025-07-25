from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.delete_all_cookies()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

URL = "https://www.saucedemo.com/inventory.html"
assert driver.current_url == URL, f"Expected URL {URL}, but got {driver.current_url}"
sleep(3)


driver.quit()
