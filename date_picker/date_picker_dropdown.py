from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

calender = driver.find_element(By.XPATH, "//input[@id='departon']")
calender.click()
month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month.select_by_visible_text("Sep")
year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
year.select_by_visible_text("2025")

days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//td/a")
for day in days:
    if day.text == "6":
        day.click()
        break

print(f"Selected data is: {calender.get_attribute('value')}")

sleep(3)
driver.quit()
