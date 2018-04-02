import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

print('Retrieving: ', url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for i in range(count):
  print('Retrieving: ', tags[position].get('href', None))
  html = urllib.request.urlopen(tags[position].get('href')).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')