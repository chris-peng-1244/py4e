import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

url = input('Enter url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
trList = soup.find_all('tr')
sum = 0
for tr in trList:
  nums = re.findall(r'\d+', tr.get_text())
  if (len(nums) == 1):
    sum = sum + int(nums[0])

print(sum)