# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times
# and report the last name you find.

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Jay.html
# Find the link at position 18 (the first name is 1).
# Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: R

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter-')

numbers = int(input('Enter count:'))
position = int(input('Enter position:'))
n = 0
count = 0
while(n < numbers):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    count = 0
    tags = soup('a')
    for tag in tags:
        count = count + 1
        if count == 18:
            x = tag.get('href', None)
            print('Retrieving:', x)
            break
    n = n+1

