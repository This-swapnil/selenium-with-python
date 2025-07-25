from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)


driver.get("https://www.saucedemo.com/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.quit()
