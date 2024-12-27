from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("head mode")
chrome_options.add_argument("--start-maximized")
service_obj = Service("C:/Users/rawradx/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://www.flipkart.com/")