import urllib.request, urllib.parse
import json

geoCodeUrl = "http://py4e-data.dr-chuck.net/geojson?"
location = input("Enter location: ")
url = geoCodeUrl + urllib.parse.urlencode({'address':location})
print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")
try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print("====Retrieve failed=====")
    print(data)
    exit(1)
print("Place id", js['results'][0]['place_id'])