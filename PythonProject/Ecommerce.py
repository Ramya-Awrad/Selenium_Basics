import time


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/rawradx/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
url = "https://www.flipkart.com/"
driver.get(url)


try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)


    first_product = driver.find_element(By.XPATH,"//body/div[@id='container']/div/div[@class='nt6sNV JxFEK3 _48O0EI']/div[@class='DOjaWF YJG4Cf']/div[@class='DOjaWF gdgoEp']/div[2]/div[1]/div[1]/div[1]/a[1]/div[2]/div[1]/div[2]")
    first_product.click()
    time.sleep(3)

    add_to_cart = driver.find_element(By.XPATH, "button[class='QqFHMw vslbG+ In9uk2']")
    add_to_cart.click()
    time.sleep(3)

    cart = driver.find_element(By.XPATH, "//a[@class='_9Wy27C']")
    cart.click()
    time.sleep(3)

    print("Product added to cart successfully")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()


