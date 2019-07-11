#!/usr/bin/python3

import requests, re
from bs4 import BeautifulSoup

url = 'https://www.rpaerobiologia.com/boletim-polinico'

content = requests.get(url)

soup = BeautifulSoup(content.text, features="html.parser")

forecast = []

for div in soup.findAll('div', {'class': 'description'}):
    forecast.append(div.text.strip())

"""
for key in forecast:
    print(key)
"""
print('===========================')
dates = re.search(('informa.*.'), forecast[0])
print(dates.group())

town = input("Localização: ")
print('===========================')
for key in forecast:
    result = re.search('.*'+town+'.*', key, re.IGNORECASE)
    #print(result.string[result.start():result.end()])
    print(result.group())

