from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://nilesh-g.github.io/learn-web/HTML/demo08.html")

print("Page Title ", driver.title)

driver.implicitly_wait(5)
list_item = driver.find_elements(By.TAG_NAME, "li")
for item in list_item:
    print(item.text)

driver.quit()    