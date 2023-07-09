from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com.br/")

search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("iPhone 14 Pro Max 1TB")
search_box.send_keys(Keys.ENTER)

time.sleep(30)
driver.quit()