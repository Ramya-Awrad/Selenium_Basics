from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

URL = "https://practicetestautomation.com/practice-test-login/"
username = "student"
password = "Password123"

# Path to your chromedriver
service_obj = Service("C:/Users/RAMYA AWRAD/Documents/chromedriver-win64/chromedriver.exe")

# Create WebDriver instance
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get(URL)

#enter login details 
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

time.sleep(5)

#check in if login success
if "logged-in-successfully" in driver.current_url:
    print("login successfull, test passed")
else:
    print("login failed, Test failed")

driver.quit()



