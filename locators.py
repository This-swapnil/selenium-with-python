from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(30)

# Open URL
driver.get("https://demo.nopcommerce.com/")

# ID
# driver.find_element(By.ID, "small-searchterms").send_keys("iphone 16")

# link-text and partial-link-text
# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.LINK_TEXT, "Regi").click()

# tag-name
"""
anchor_elements = driver.find_elements(By.TAG_NAME, "a")
links = [
    a.get_attribute("href")
    for a in anchor_elements
    if a.get_attribute("href") is not None
]

for link in links:
    print(link)
"""

# CSS selectors
# driver.find_element(By.CSS_SELECTOR, "#small-searchterms").send_keys("iphone 16")

# XPATH
# Syntax ==> //tagname[@attribute=value]
driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys("iphone 16")
driver.find_element(
    By.XPATH, "//button[text()='Search' or class='button-1 search-box-button']"
).click()  # xpath with "or" option


sleep(3)
# Quit browser
driver.quit()
