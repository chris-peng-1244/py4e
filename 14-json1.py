import urllib.request
import json

url = input("Enter location: ")
print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()
js = json.loads(data)
print("Retrieved", len(data), "characters")
print("Count:", len(js['comments']))
print("Sum:", sum([int(item['count']) for item in js['comments']]))