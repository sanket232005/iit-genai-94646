from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")

print("Initial Page Tiltle",driver.title)

driver.implicitly_wait(5)

serch_box = driver.find_element(By.NAME, "q")
serch_box.send_keys("dkte college ichalkaranji")
serch_box.send_keys(Keys.RETURN)

print("Later Page Title ",driver.title)
time.sleep(10)
driver.quit()