from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://jqueryui.com/droppable/")

driver.switch_to.frame(0)

src = driver.find_element(By.XPATH, "//div[@id='draggable']")
dest = driver.find_element(By.XPATH, "//div[@id='droppable']")

act = ActionChains(driver)
act.drag_and_drop(src, dest).perform()

sleep(3)
driver.quit()
