from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider = driver.find_element(
    By.XPATH, "//body//div//span[1]"
)  # {'x': 278, 'y': 195}
max_slider = driver.find_element(
    By.XPATH, "//body//div//span[2]"
)  # {'x': 300, 'y': 196}

print(f"Location of Min slider before moving: {min_slider.location}")
print(f"Location of Max slider before moving: {max_slider.location}")

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -96, 0).perform()

print(f"Location of Min slider after moving: {min_slider.location}")
print(f"Location of Max slider after moving: {max_slider.location}")

sleep(3)
driver.quit()
