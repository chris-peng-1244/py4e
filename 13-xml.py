from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input("Enter location:")
print('Retrieving', url)
h = urllib.request.urlopen(url)
xml = h.read()
print('Retrieved', len(xml), 'characters')
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
print('Count:', len(counts))
print('Sum', sum([int(c.text) for c in counts]))
