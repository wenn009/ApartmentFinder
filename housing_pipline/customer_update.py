import os
import sys
import json
from twilio.rest import Client

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client

ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
TWILIO_PHONE_NUMBER = "+15162178352"

CUSTOMER_TABLE_NAME = 'customers'
PRICE_MAP = {
    1: 1000,
    2: 1500,
    3: 2000,
    4: 2500,
    5: 3000
}

def getCustomers():
    db = mongodb_client.get_db('customer_infor')
    return db[CUSTOMER_TABLE_NAME].find();

def send_update(customers, house):
    for customer in customers:
        if customer['zipcode'] == house['zipcode']:
            if customer['near_station'] == house['nearStation']:
                house_price = int(house['price'][1:])
                if house_price < PRICE_MAP[customer['price_range']] and house_price > (PRICE_MAP[customer['price_range']] - 500):
                    #text
                    TWILIO_CLIENT.messages.create(
                        to = customer['telephone'],
                        from_ = TWILIO_PHONE_NUMBER,
                        body = "Hi " + customer['name'] + " We found this apartment for you:\n" 
                        + house['name'] + "\n" + house['price'] + "\n" 
                        + house["where"] + house['zipcode'] + "\n" + house["url"]
                        )
                    print "sent message to client"
                    

''' Test Data '''
'''
house = {
    'name': 'BAY RIDGE__BAY RIDGE__ FREE LAUNDRY__STORAGE__NEWLY RENOVATED__PETS OK', 
    'area': None, 
    'url': 'https://newyork.craigslist.org/brk/fee/d/bay-ridgebay-ridge-free/6320917934.html', 
    'has_map': True, 
    'price': '$1999', 
    'bedrooms': '2', 
    'zipcode': '11210', 
    'geotag': [40.633721, -74.021652], 
    'nearStation': True, 
    'image_url': 'https://maps.googleapis.com/maps/api/streetview?fov=90&pitch=0&key=AIzaSyCkpVrJULDUUBqQEVd_pqK6lIpAkcsQ8Bs&size=400x400&location=40.633721,-74.021652',
    'has_image': True,
    'datetime': 
    '2017-09-25 17:57',
    'where': 
    'BAY RIDGE__BAY RIDGE__BAY RIDGE__', 
    'id':  '6320917934'
}   
customers = getCustomers()
send_update(customers, house)
'''
