from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()


admin = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
usermgmt = driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
users = driver.find_element(By.XPATH, "//a[normalize-space()='Users']")

# MouseHover
act = ActionChains(driver=driver)
act.move_to_element(admin).move_to_element(usermgmt).move_to_element(
    users
).click().perform()
