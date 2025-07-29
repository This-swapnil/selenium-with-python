from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.nopcommerce.com/")

# 1) Click on the link
driver.find_element(By.LINK_TEXT, "Digital downloads").click()

# Find total no of links present on webpage
links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total no of links: {len(links)}")

# 2) Print all the link names
for link in links:
    print(link.text)


sleep(3)
driver.quit()
