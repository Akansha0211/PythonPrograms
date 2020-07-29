## SCRAPING HTML DATA WITH BEAUTIFUL SOUP

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter-')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
sum = 0
tags = soup('span')
for tag in tags:
    y = str(tag)
    x = re.findall('[0-9]+',y)
    for i in x:
        i = int(i)
        sum = sum + i
print(sum)



