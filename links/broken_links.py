from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("http://www.deadlinkcity.com/")

links = driver.find_elements(By.TAG_NAME, "a")
count = 0

# get the href attribute
for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(f"{url} is a broken link")
        count += 1
    else:
        print(f"{url} is valid link")

print(f"Total borken links are: {count}")
