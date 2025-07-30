from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# 1) Scroll down page by pixel
"""
driver.execute_script("window.scrollBy(0,3000)", "")
value = driver.execute_script("return window.pageYOffset;")
print(f"No of pixels moved: {value}")
"""


# 2) Scroll down page till the element is visible
"""
ele = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();", ele)
value = driver.execute_script("return window.pageYOffset;")
print(f"No of pixels moved: {value}")
"""

# 3) Scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
value = driver.execute_script("return window.pageYOffset;")
print(f"No of pixels moved: {value}")


# 4) Scroll upto starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight);")
value = driver.execute_script("return window.pageYOffset;")
print(f"No of pixels moved: {value}")

sleep(3)
driver.quit()
