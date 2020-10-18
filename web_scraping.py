# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:39:35 2020

@author: jpuig
"""

import requests
from bs4 import BeautifulSoup



page = requests.get("https://www.google.com")

soup = BeautifulSoup(page.content)


head_tag = soup.head.text
print(soup.head)
print(soup.head.text)

body_tag = soup.body

print(body_tag.contents)




for child in body_tag.children:
    print(child)



print(soup.prettify())

"""
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b 
type(tag)

tag.name
tag.attrs

print(tag.name)
print(tag.attrs)

"""

