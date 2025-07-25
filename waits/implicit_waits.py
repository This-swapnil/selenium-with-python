from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


# Implicit wait
driver.implicitly_wait(30)

driver.get("https://www.bing.com/")

searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()

driver.find_element(
    By.XPATH, "//h2[@class=' b_topTitle']//a[normalize-space()='Selenium']"
).click()


sleep(2)
driver.quit()
