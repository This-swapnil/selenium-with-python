from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
countries_list = driver.find_elements(
    By.XPATH, "//ul[@id='select2-billing_country-results']/li"
)

print(f"Total countries: {len(countries_list)}")

for country in countries_list:
    if country.text == "Mali":
        country.click()
        break

sleep(3)
driver.quit()
