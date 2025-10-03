from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your chromedriver
service_obj = Service("C:/Users/RAMYA AWRAD/Documents/chromedriver-win64/chromedriver.exe")

# Create WebDriver instance
driver = webdriver.Chrome(service=service_obj)

# Open Google
driver.get("https://www.google.com")
print("Title is:", driver.title)

# Wait and close
time.sleep(3)
driver.quit()