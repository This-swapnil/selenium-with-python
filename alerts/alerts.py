from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# driver.find_element(
#     By.XPATH, "//button[normalize-space()='Click for JS Alert']"
# ).click()
# sleep(2)
# alert_window = driver.switch_to.alert
# print(alert_window.text)
# alert_window.accept()

driver.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Prompt']"
).click()
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("Welcome")
alert_window.accept()

sleep(3)
driver.quit()
