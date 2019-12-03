from Python_Automation_Testing import config
import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)

"""authors = soup.find_all('small', class_='author')
print("The authors are: ")
for author in authors:
    print(author.text)"""
