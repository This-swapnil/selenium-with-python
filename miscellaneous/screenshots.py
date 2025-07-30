from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://demo.nopcommerce.com/")

# driver.save_screenshot("miscellaneous//demo_nopcommerce.png")
# driver.get_screenshot_as_file("miscellaneous//demo_nopcommerce1.png")

driver.find_element(
    By.XPATH, "//img[@title='Show details for Apple MacBook Pro']"
).screenshot("miscellaneous/macbook_image.png")

driver.quit()
