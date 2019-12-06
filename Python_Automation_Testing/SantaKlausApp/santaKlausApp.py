from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

emails1 = ['scarlatalinn@gmail.com;', 'andrada.marin5@gmail.com;', 'Dragosdm22@gmail.com;', 'andrei.tenea93@gmail.com;', 'andreea.madalinavulpe@gmail.com;', 'robert.buica@gmail.com;', 'roxana.barran@yahoo.ro;', 'denisa_vatulescu@yahoo.com;', 'alex.dragomir95@yahoo.com;', 'mc@gmail']
names1 = ['Ionut', 'Andrada', 'Dragos', 'Andrei', 'Andreea', 'Robert', 'Roxana', 'Denisa', 'Alex', 'Cristi']

emails = ['scarlatalinn@gmail.com;', 'test2@email.com', 'c']
names = ['Ionut', 'TEst2name', 'h']
#print(emails)


def pop_random(emails):
    idx = random.randrange(0, len(emails))
    return emails.pop(idx)

pairs = []

while len(emails) > 0:
    rand1 = pop_random(emails)
    rand2 = pop_random(names)
    pair = rand1, rand2
    pairs.append(list(pair))


print('Pairs:')
for i in pairs:
   print(i)
for x in pairs:
    for a in x:
        print(a)

    '''
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


#driver.implicitly_wait(15)
#time.sleep(5)

try:
    send_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=":45"]/div/div'))
        )
    send_button.click()
finally:
    print('send button')

"""
WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=":9o"]'))
        )"""
driver.implicitly_wait(15)
time.sleep(5)
for email in emails:
    to_address = driver.find_element_by_xpath('//*[@id=":9o"]').send_keys(email)

driver.implicitly_wait(15)
subject_email = driver.find_element_by_xpath('//*[@id=":96"]')
subject_email.send_keys('Santa Klaus Automated')

driver.implicitly_wait(15)
body_text = driver.find_element_by_xpath('//*[@id=":ab"]')
body_text.send_keys('Va saluta Santa Klaus Ionutii!')

driver.implicitly_wait(15)
send_button2 = driver.find_element_by_xpath('//*[@id=":8w"]')
send_button2.click()
'''

