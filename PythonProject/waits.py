import time

from selenium.webdriver import Keys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/rawradx/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(15)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
flipkart_search = driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
flipkart_search.send_keys("Mobile")
flipkart_search.send_keys(Keys.RETURN)
driver.find_element(By.XPATH,"//div[normalize-space()='SAMSUNG Galaxy S23 5G (Cream, 128 GB)']").click()
time.sleep(5)
driver.quit()