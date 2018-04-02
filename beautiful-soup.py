import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = [ tag.get('href', None) for tag in soup('a') ]
print([ tag for tag in tags if re.match(r'^https?', tag) ])