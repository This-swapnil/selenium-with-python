from time import sleep
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.saucedemo.com/")
driver.get("https://demo.nopcommerce.com/")

driver.back()
sleep(3)
driver.forward()
sleep(3)
driver.refresh()
sleep(3)


driver.quit()
