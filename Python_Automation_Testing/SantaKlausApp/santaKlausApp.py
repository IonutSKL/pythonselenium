from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('D:\chromedriver')
driver.get('https://mail.google.com/mail/u/0/#inbox')
driver.maximize_window()




login_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
login_email.send_keys('santaklausautomation@gmail.com')

submit_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
submit_button.click()

driver.implicitly_wait(5)

password_email = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_email.send_keys('SantaKlaus1234#')
password_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
password_button.click()

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="bhlf"]/input[2]'))
        )
html_simple = driver.find_element_by_xpath('//*[@id="bhlf"]/input[2]').click()
#driver.implicitly_wait(15)
#time.sleep(5)

try:
    send_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=":45"]/div/div'))
        )
    send_button.click()
finally:
    print('send button')

emails = 'scarlatalinn@gmail.com;  andrada.marin5@gmail.com;Dragosdm22@gmail.com;andrei.tenea93@gmail.com;andreea.madalinavulpe@gmail.com;robert.buica@gmail.com;roxana.barran@yahoo.ro;denisa_vatulescu@yahoo.com;alex.dragomir95@yahoo.com'
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=":9o"]'))
        )
to_address = driver.find_element_by_xpath('//*[@id=":9o"]').send_keys(emails)
