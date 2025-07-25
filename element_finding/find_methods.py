from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demo.nopcommerce.com/")

""" find_element() ==> Returns single webelement """

# 1) Locator matching with single  webelement

"""
element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
element.send_keys("Apple macbook pro 13-inch")
"""

# 2) Locator matching with multiple webelement
"""
element = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(element.text)
"""

# 3) Element not available then throw NoSuchElementException
"""
driver.find_element(By.XPATH, "//div[@class='foter']")
"""


""" find_elements() ==> Returns multiple webelement """
# 1) Locator matching with single  webelement ==> it returns the list of webelements
"""
elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
elements[0].send_keys("Apple macbook pro 13-inch")
"""

# 2) Locator matching with multiple webelement
"""
elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(f"Total elements present in a list: {len(elements)}")
for element in elements:
    print(element.text)
"""

# 3) Element not available then throw NoSuchElementException
elements = driver.find_elements(By.XPATH, "//div[@class='foter']")
print(f"Total elements present in a list: {len(elements)}")

sleep(2)
driver.quit()
