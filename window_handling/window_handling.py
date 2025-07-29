from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# windowid = driver.current_window_handle
# print(windowid)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowids = driver.window_handles

# Approach 1
"""
parent_window_id = windowids[0]
child_window_id = windowids[1]
print(f"Parent windw id: {parent_window_id} and Child window id: {child_window_id}")

driver.switch_to.window(child_window_id)
print(f"Title of the child window: {driver.title}")

driver.switch_to.window(parent_window_id)
print(f"Title of the parent window: {driver.title}")
"""


# Approach 2
for winid in windowids:
    driver.switch_to.window(winid)
    print(f"Title of the page is: {driver.title}")


driver.quit()
