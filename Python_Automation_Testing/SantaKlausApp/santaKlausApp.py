from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

emails = ['scarlatalinn@gmail.com', 'andrada.marin5@gmail.com', 'dragosdm22@gmail.com', 'andrei.tenea93@gmail.com', 'andreea.madalinavulpe@gmail.com', 'robert.buica@gmail.com', 'roxana.barran@yahoo.ro', 'denisa_vatulescu@yahoo.com', 'alex.dragomir95@yahoo.com', 'christian.cuna89@gmail.com']
names = ['Ionut', 'Andrada', 'Dragos', 'Andrei', 'Andreea', 'Robert', 'Roxana', 'Denisa', 'Alex', 'Cristi']

#emails1 = ['scarlatalinn@gmail.com', 'denisa_vatulescu@yahoo.com']
#names = ['Ionut', 'Denisa']
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
#to do
#def check_pairs(pairs):

print('Santa Klaus Match:')
#for i in pairs:
 #  print(i)
for x in pairs:
    print(x[0], 'will be Santa Klaus for: ', x[1])


driver = webdriver.Chrome('D:\chromedriver')
driver.get('https://mail.google.com/mail/u/0/h/prfn4k4j6fjk/?zy=e&f=1')
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

"""
WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id=":9o"]'))
        )"""


def match_emails(email):
        try:
            send_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located( (By.XPATH, '/html/body/table[3]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td/b/a'))
            )
            send_button.click()
        finally:
            print('send button')
        #to_address = driver.find_element_by_xpath('//*[@id=":9o"]')
        to_address = driver.find_element_by_name('to')
        to_address.click()
        to_address.send_keys(email[0])
        #print('to address here')
        subject_email = driver.find_element_by_name('subject')
        subject_email.send_keys('Santa Klaus Automated')
        #print( 'subject here' )
        body_text = driver.find_element_by_name( 'body' )
        body_text.send_keys('You will be Santa Klaus for: ')
        body_text.send_keys(email[1])
        #print( 'body text here' )
        send_button2 = driver.find_element_by_name( 'nvp_bu_send' )
        send_button2.click()
        #print( 'send button 2 here' )

'''
def match_emails2(email):
    try:
        send_button = WebDriverWait( driver, 10 ).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/table[3]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td/b/a') )
        )
        send_button.click()
    finally:
        print( 'send button' )
    # to_address = driver.find_element_by_xpath('//*[@id=":9o"]')
    to_address = driver.find_element_by_name( 'to' )
    to_address.click()
    to_address.send_keys( email[1] )
    # print('to address here')
    subject_email = driver.find_element_by_name( 'subject' )
    subject_email.send_keys( 'Santa Klaus Automated' )
    # print( 'subject here' )
    body_text = driver.find_element_by_name( 'body' )
    body_text.send_keys( 'You will be Santa Klaus for: ' )
    body_text.send_keys( email[0] )
    # print( 'body text here' )
    send_button2 = driver.find_element_by_name( 'nvp_bu_send' )
    send_button2.click()
    # print( 'send button 2 here' )'''


def send_emails():
    for email in pairs:
        match_emails(email)
        #match_emails2(email)


send_emails()

driver.close()