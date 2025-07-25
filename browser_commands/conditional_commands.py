from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)


driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

# Conditional commandds


input_username = driver.find_element(By.ID, "FirstName")

# 1. is_displayed()
print(f"input_username is displayed? {input_username.is_displayed()}")

# 2. is_enabled()
print(f"input_username is enabled? {input_username.is_enabled()}")

# 3. is_selected
rd_button = driver.find_element(By.ID, "gender-male")
print(rd_button.is_selected())
rd_button.click()
print(rd_button.is_selected())


# Browser commands
# driver.close()
driver.quit()
