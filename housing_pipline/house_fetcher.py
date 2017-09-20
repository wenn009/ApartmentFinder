import os
import sys
import redis



sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import craiglist_fetcher

NEW_YORK_STATE = 'newyork'
BROOKLYN_CITY = 'brk'
BRK_ZIP_CODES = ["06234","11201","11202","11203","11204","11205","11206","11207","11208","11209","11210","11211","11212","11213","11214","11215","11216","11217","11218","11219","11220","11221","11222","11223","11224","11225","11226","11228","11229","11230","11231","11232","11233","11234","11235","11236","11237","11238","11239","11241","11242","11243","11245","11247","11249","11251","11252","11256","18813","42261","44144","52211","55746","36429","39425","46111","49230","53521","62059","21225","21226","11240","11244","11248","11254","11255"]
zipcodes2 = ["11229","11230","11231","11232","11233","11234","11235","11236","11237","11238","11239","11241","11242","11243","11245","11247","11249","11251","11252","11256","18813","42261","44144","52211","55746","36429","39425","46111","49230","53521","62059","21225","21226","11240","11244","11248","11254","11255"]
from cloud_amqp_client import CloudAMQPClient

SCRAPE_HOUSING_QUEUE_URL = 'amqp://tebodcbi:SaF4IwTvyZIm6HlRQuMu0gV0jdbOnLBJ@rhino.rmq.cloudamqp.com/tebodcbi'
SCRAPE_HOUSING_QUEUE_NAME = 'houses_scrape_queue'

cloudamqp_client = CloudAMQPClient(SCRAPE_HOUSING_QUEUE_URL, SCRAPE_HOUSING_QUEUE_NAME)

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
HOUSES_TIME_OUT_IN_SECONDS = 3600 * 24 * 5
SESSION_PATH = '/craiglist_houses/'

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)

while True:
    num_houses = 0
    for zip_code in zipcodes2:
        houses_list = craiglist_fetcher.fetchHousing(NEW_YORK_STATE, BROOKLYN_CITY, zip_code)

        for result in houses_list.get_results(sort_by='newest', geotagged=True, limit=20):
            if redis_client.get(SESSION_PATH+result['id']) is None:
                
                result['zipcode'] = zip_code #add zip code to result object
                print result
                num_houses += 1
                
                redis_client.set(SESSION_PATH+result['id'], 'true')
                redis_client.expire(SESSION_PATH+result['id'], HOUSES_TIME_OUT_IN_SECONDS)
                
                cloudamqp_client.send_message(result)

    print 'fetch %d of houses: ' % num_houses 
    cloudamqp_client.sleep(SLEEP_IN_SECONDS)

