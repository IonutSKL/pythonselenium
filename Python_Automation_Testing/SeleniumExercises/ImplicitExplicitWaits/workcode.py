from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('D:\chromedriver')
driver.implicitly_wait(10)
driver.get('http://www.python.org')
driver.maximize_window()

my_element = driver.find_element_by_id('start-shell')
print(my_element)
driver.close()
"""
try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "python-logo"))
    )
finally:
    driver.quit()
"""