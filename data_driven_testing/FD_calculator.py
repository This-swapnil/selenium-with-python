from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from data_driven_testing import xlutils
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)


driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html"
)

principle = driver.find_element(By.XPATH, "//input[@id='principal']")
rate_of_interest = driver.find_element(By.XPATH, "//input[@id='interest']")
period_count = driver.find_element(By.XPATH, '//input[@id="tenure"]')
period_duration = driver.find_element(By.XPATH, "//select[@id='tenurePeriod']")
frequency = driver.find_element(By.XPATH, "//select[@id='frequency']")
calculate = driver.find_element(
    By.XPATH,
    "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']",
)
clear = driver.find_element(By.XPATH("//img[@class='PL5']"))

# get an Excel file path
file = "Data/CalData.xlsx"

rownum = xlutils.get_row_count(file=file, sheet_name="Sheet1")
colnum = xlutils.get_column_count(file=file, sheet_name="Sheet1")

for i in range(2, rownum + 1):
    princ = xlutils.read_data(file, "Sheet1", i, 1)
    roi = xlutils.read_data(file, "Sheet1", i, 2)
    per1 = xlutils.read_data(file, "Sheet1", i, 3)
    per2 = xlutils.read_data(file, "Sheet1", i, 4)
    freq = xlutils.read_data(file, "Sheet1", i, 5)
    exp_mavalue = xlutils.read_data(file, "Sheet1", i, 6)

    # passing data to application
    principle.send_keys(princ)
    rate_of_interest.send_keys(roi)
    period_count.send_keys(per1)
    Select(period_duration).select_by_visible_text(per2)
    Select(frequency).select_by_visible_text(freq)
    calculate.click()

    act_value = driver.find_element(By.xpath, "//span[@id='resp_matval']//strong").text

    if float(act_value) == float(exp_mavalue):
        print("Test Passed!")
        xlutils.write_data(file, "Sheet1", i, 8, "Passed")
        xlutils.fill_green_color(file, "Sheet1", i, 8)
    else:
        print("Test Failed!")
        xlutils.write_data(file, "Sheet1", i, 8, "Failed")
        xlutils.fill_red_color(file, "Sheet1", i, 8)

    clear.click()
    sleep(2)

driver.quit()
