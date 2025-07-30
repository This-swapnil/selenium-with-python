from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)


driver.get("https://demo.nopcommerce.com/")

# regilink = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(regilink) old way to open the link in new tab

# Tab
# driver.switch_to.new_window("tab")
# driver.get("https://www.google.co.in")


# Window
driver.switch_to.new_window("window")
driver.get("https://www.google.co.in")


sleep(3)
driver.quit()
