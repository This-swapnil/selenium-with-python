from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)


driver.get("https://testautomationpractice.blogspot.com/")

drp_country = Select(driver.find_element(By.XPATH, "//select[@id='country']"))

# select options form the dropdown
# drp_country.select_by_visible_text("India")
# drp_country.select_by_value("canada")  # Canada
# drp_country.select_by_index(0)  # United States

# Capture all the options and print them
# options = drp_country.options
# print(f"Total no of options: {len(options)}")
# print("Options are: ")
# for opt in options:
#     print(opt.text)

# Select option from dropdown without using built-in method
options = drp_country.options
for opt in options:
    if opt.text == "India":
        opt.click()
        break

sleep(3)
driver.quit()
