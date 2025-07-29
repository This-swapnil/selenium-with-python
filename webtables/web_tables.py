# 1) Count number of rows and columns
# 2) Read specific row & columns data
# 3) Read all the rows & columns data
# 4) Read data based on condition(List books name whose author is Mukesh)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://testautomationpractice.blogspot.com/")


# 1) Count number of rows and columns
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print(f"Total rows in table: {len(rows)}")
cols = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
print(f"Total no of columns: {len(cols)}")


# 2) Read specific row & columns data
"""
book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]//td[1]").text
print(f"Book Name: {book_name}")
"""

# 3) Read all the rows & columns data
"""
for r in range(2, len(rows) + 1):
    for c in range(1, len(cols) + 1):
        cell = driver.find_element(
            By.XPATH, f"//table[@name='BookTable']//tr[{r}]//td[{c}]"
        ).text
        print(cell, end="\t\t")
    print()
"""

# 4) Read data based on condition(List books name whose author is Mukesh)
for r in range(2, len(rows) + 1):
    author = driver.find_element(
        By.XPATH, f"//table[@name='BookTable']//tr[{r}]//td[2]"
    ).text
    if author == "Mukesh":
        bookname = driver.find_element(
            By.XPATH, f"//table[@name='BookTable']//tr[{r}]//td[1]"
        ).text
        print(f"Book name: {bookname} and author is: {author}")

driver.quit()
