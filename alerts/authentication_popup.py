from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.quit()
