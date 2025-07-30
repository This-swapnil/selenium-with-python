from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demoqa.com/buttons")

btn = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")

act = ActionChains(driver)

act.double_click(btn).perform()

sleep(3)
driver.quit()
