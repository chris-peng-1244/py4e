import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

def getTagsFromUrl(url):
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  return tags

print('Retrieving: ', url)
tags = getTagsFromUrl(url)
for i in range(count):
  print('Retrieving: ', tags[position].get('href', None))
  tags = getTagsFromUrl(tags[position].get('href'))
