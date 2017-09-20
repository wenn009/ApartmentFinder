
import urllib

APIKEY = 'AIzaSyCkpVrJULDUUBqQEVd_pqK6lIpAkcsQ8Bs'
ADDRESS = 'https://maps.googleapis.com/maps/api/streetview?'

SIZE = '400x400'
FOV = 90
PITCH = 0


def generate_house_image(geo):
    payload = {
        'size': SIZE,
        'fov': 90,
        'pitch': 0,
        'key': APIKEY
    }
    geo_str = (str(geo)[1:-1]).replace(" ", "")
    locations = "&location=%s" % geo_str
    #r = requests.get(ADDRESS, params=payload)
    #print r.text
    print(ADDRESS + urllib.urlencode(payload) + locations)


#generate_house_image(result['geotag'])
