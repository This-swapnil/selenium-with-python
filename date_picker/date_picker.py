from datetime import date
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://jqueryui.com/datepicker/")

# switch to frame
driver.switch_to.frame(0)

# date format mm/dd/yyyy

# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("07/31/2025")

date_picker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
date_picker.click()
month = "September"
year = "2025"
day = "6"

# select month and year
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        driver.find_element(
            By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']"
        ).click()

# select day
dates = driver.find_elements(
    By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody//a"
)
for d in dates:
    if d.text == day:
        d.click()
        break

sleep(3)
driver.quit()
