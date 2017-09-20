import os
import sys
import json
from geopy.distance import vincenty


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'. 'common', 'mta_stations'))

from cloud_amqp_client import CloudAMQPClient
import mongo_client

SCRAPE_HOUSING_QUEUE_URL = 'amqp://tebodcbi:SaF4IwTvyZIm6HlRQuMu0gV0jdbOnLBJ@rhino.rmq.cloudamqp.com/tebodcbi'
SCRAPE_HOUSING_QUEUE_NAME = 'houses_scrape_queue'
SLEEP_TIME_IN_SECONDS = 5

cloudamqp_client = CloudAMQPClient(SCRAPE_HOUSING_QUEUE_URL, SCRAPE_HOUSING_QUEUE_NAME)
STATIONS_JSON = open('../common/mta_stations').read()
STATIONS = json.loads(STATIONS_JSON)
MAX_TRANSIT_DIST = 250 # meters

HOUSES_TABLE_NAME = 'houses'

def handleMsg(msg):
    if msg is not None or isinstance(msg, dict):
        #TO DO
        task = msg
        if(isNearStation(task['geotag'])):
            task['nearStation'] = True

        db = mongo_client.get_db()
        db[HOUSES_TABLE_NAME].replace_one({'id': task['id']}, task, upsert=True)
    else:
        print 'Message is broken'
        return

isNearStation(geo):
    for station in STATIONS:
        location = (station[0], station[1])
        if (vincenty(geo, location).meters) > MAX_TRANSIT_DIST:
            return True
    return False


while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.get_message()
        if msg is not None:
            try:
                 handleMsg(msg)
            except Exception as e:
                 print e
                 pass
        cloudamqp_client.sleep(SLEEP_TIME_IN_SECONDS) 

'''{'name': u'Newly renovated 2 bedroom, close to Manhattan', 'area': u'750ft2', 'url': u'https://newyork.craigslist.org/brk/abo/d/newly-renovated-2-bedroom/6306455207.html', 'where': u'Dyker Height', 'price': u'$1750', 'bedrooms': u'2', 'zipcode': '11228', 'geotag': (40.623145, -74.004476), 'has_image': True, 'datetime': u'2017-09-14 22:20', 'has_map': True, 'id': u'6306455207'}
[x] Sent message to houses_scrape_queue: {'name': u'Newly renovated 2 bedroom, close to Manhattan', 'area': u'750ft2', 'url': u'https://newyork.craigslist.org/brk/abo/d/newly-renovated-2-bedroom/6306455207.html', 'where': u'Dyker Height', 'price': u'$1750', 'bedrooms': u'2', 'zipcode': '11228', 'geotag': (40.623145, -74.004476), 'has_image': True, 'datetime': u'2017-09-14 22:20', 'has_map': True, 'id': u'6306455207'}
{'name': u'$1,450.00 One bedroom w/ parking spot', 'area': u'750ft2', 'url': u'https://newyork.craigslist.org/brk/fee/d/one-bedroom-parking-spot/6305863749.html', 'where': u'dyker heights', 'price': u'$1450', 'bedrooms': u'1', 'zipcode': '11228', 'geotag': (40.613339, -74.011086), 'has_image': True, 'datetime': u'2017-09-14 13:29', 'has_map': True, 'id': u'6305863749'}
[x] Sent message to houses_scrape_queue: {'name': u'$1,450.00 One bedroom w/ parking spot', 'area': u'750ft2', 'url': u'https://newyork.craigslist.org/brk/fee/d/one-bedroom-parking-spot/6305863749.html', 'where': u'dyker heights', 'price': u'$1450', 'bedrooms': u'1', 'zipcode': '11228', 'geotag': (40.613339, -74.011086), 'has_image': True, 'datetime': u'2017-09-14 13:29', 'has_map': True, 'id': u'6305863749'}'''