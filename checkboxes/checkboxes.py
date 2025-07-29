from operator import le
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://testautomationpractice.blogspot.com/")

# 1) select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()


# 2) select all checkboxes

days = driver.find_elements(
    By.XPATH, "//input[@class='form-check-input'][@type='checkbox']"
)

print(f"Total checkboxes available for days are: {len(days)}")
# days=driver.find_elements(By.XPATH,"//input[@type="checkbox" and contains(@id,'day')]")   => same xpath with contains function
for day in days:
    sleep(1)
    day.click()


# 3) Select specific checkboxes
"""for day in days:
    week_name = day.get_attribute("id")
    if week_name in ["monday", "sunday"]:
        sleep(1)
        day.click()"""
# 4) Select last 2 checkboxes
"""
for i in range(len(days) - 2, len(days)):
    days[i].click()
"""

# 5) Select first 2 checkboxes
"""
for i in range(len(days) - 5):
    days[i].click()
"""


# 6) clear all checkboxes
for day in days:
    if day.is_selected():
        day.click()


sleep(3)
driver.quit()
