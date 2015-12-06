import urllib, json


LAT = 120.9911108
LNG = 14.5960339
AUTH_KEY = 'place_your_api key_here'
LOCATION = str(LNG) + "," + str(LAT)
RADIUS = 41000 
TYPES = 'gas_station' 
BASE_URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    '?location=%s'
    '&radius=%s'
    '&types=%s'
    '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)

def get_json(url):
    response = urllib.urlopen(url)
    json_raw = response.read()
    json_data = json.loads(json_raw)
    return json_data

url = BASE_URL
while True:
    result = get_json(url)
    if result['status'] == 'OK':
        for place in result['results']:
            print place['name'], place['geometry']['location']['lat'], \
                place['geometry']['location']['lng']
        if 'next_page_token' in result:
            url = BASE_URL + '&pagetoken=' + result['next_page_token']
        else:
            break
