import os
import sys
import json
from geopy.distance import vincenty


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common', 'mta_stations'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common', 'google_image'))

from cloud_amqp_client import CloudAMQPClient
import mongo_client
import obtain_image

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
        
        if(task['geotag'] is not None):
            #check if house is near station
            if(isNearStation(task['geotag'])):
                task['nearStation'] = True
            #obtain image
            task['image_url'] = obtain_image.generate_house_image(task['geotag'])

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

