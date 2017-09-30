import os
import sys
import json
from geopy.distance import vincenty
import customer_update


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common', 'mta_stations'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common', 'google_image'))

from cloud_amqp_client import CloudAMQPClient
import mongodb_client
import obtain_image

SCRAPE_HOUSING_QUEUE_URL = 'amqp://tebodcbi:SaF4IwTvyZIm6HlRQuMu0gV0jdbOnLBJ@rhino.rmq.cloudamqp.com/tebodcbi'
SCRAPE_HOUSING_QUEUE_NAME = 'houses_scrape_queue'
SLEEP_TIME_IN_SECONDS = 5

cloudamqp_client = CloudAMQPClient(SCRAPE_HOUSING_QUEUE_URL, SCRAPE_HOUSING_QUEUE_NAME)
STATIONS_JSON = open('../common/mta_stations/station_geo.json').read()
STATIONS = json.loads(STATIONS_JSON)
MAX_TRANSIT_DIST = 400 # meters

HOUSES_TABLE_NAME = 'houses'

def handleMsg(msg):
    if msg is not None or isinstance(msg, dict):
        #TO DO
        task = msg
        
        if(task['geotag'] is not None):
            #check if house is near station
            task['nearStation']= isNearStation(task['geotag'])
 
            #obtain image
            task['image_url'] = obtain_image.generate_house_image(task['geotag'])


        db = mongodb_client.get_db()
        db[HOUSES_TABLE_NAME].replace_one({'id': task['id']}, task, upsert=True)

        customers = customer_update.getCustomers()
        customer_update.send_update(customers, task)

        print task
    else:
        print 'Message is broken'
        return

def isNearStation(geo):
    for station in STATIONS:
        location = (station[1], station[0])
        #print vincenty(geo, location).meters
        if (vincenty(geo, location).meters) < MAX_TRANSIT_DIST:
            return True
    return False


while True:
    if cloudamqp_client is not None:
        msg = cloudamqp_client.get_message()
        if msg is not None:
            try:
                 handleMsg(msg)
            except Exception as e:
                 print e
                 pass
        cloudamqp_client.sleep(SLEEP_TIME_IN_SECONDS) 

