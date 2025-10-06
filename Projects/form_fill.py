from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os

# Path to your chromedriver
service_obj = Service("C:/Users/RAMYA AWRAD/Documents/chromedriver-win64/chromedriver.exe")

# Create WebDriver instance
driver = webdriver.Chrome(service=service_obj)
#maximize the window
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")

#wait = WebDriverWait(driver, 10)
time.sleep(5)

# fill name and email
driver.find_element(By.ID, "firstName").send_keys("Ramya")
driver.find_element(By.ID, "lastName").send_keys("Awrad")
driver.find_element(By.ID, "userEmail").send_keys("ramyaawrad@example.com")

# select gender (radio button)
gender = driver.find_element(By.XPATH, "//label[text()='Female']")
gender.click()

# driver.find_element(By.XPATH, "//label[text()='Female']").click()

# Enter Mobile Number
driver.find_element(By.ID, "userNumber").send_keys("9876543210")

#  Select Hobbies (checkbox)
hobby_checkbox = driver.find_element(By.XPATH, "//label[text()='Reading']")
hobby_checkbox.click()

# driver.find_element(By.XPATH, "//label[text()='Reading']").click()

# Upload File
file_path = os.path.abspath("sample_upload.txt")  # make sure file exists
driver.find_element(By.ID, "uploadPicture").send_keys(file_path)

# Scroll to Submit button & click
submit_btn = driver.find_element(By.ID, "submit")
#driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
submit_btn.click()

driver.quit()




