import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("Enter address: ")
    if len(address) < 1: break
    
    url = serviceurl + urllib.parse.urlencode({
        'address': address,
        'key': 'AIzaSyCHsCFbiF-Ji9CmP3u7aQ-4Rmj1lbg9we0'
    })

    print("Receiving url", url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        jsData = json.loads(data)
    except:
        jsData = None

    if not jsData or 'status' not in jsData or jsData['status'] != 'OK':
        print('======Retrieve failed======')
        print(data)
        continue

    print(json.dumps(jsData, indent=4))
    lat = jsData['results'][0]['geometry']['location']['lat']
    lng = jsData['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = jsData['results'][0]['formatted_address']
    print(location)