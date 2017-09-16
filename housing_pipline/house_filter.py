import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloud_amqp_client import CloudAMQPClient

SCRAPE_HOUSING_QUEUE_URL = 'amqp://tebodcbi:SaF4IwTvyZIm6HlRQuMu0gV0jdbOnLBJ@rhino.rmq.cloudamqp.com/tebodcbi'
SCRAPE_HOUSING_QUEUE_NAME = 'houses_scrape_queue'
SLEEP_TIME_IN_SECONDS = 5

cloudamqp_client = CloudAMQPClient(SCRAPE_HOUSING_QUEUE_URL, SCRAPE_HOUSING_QUEUE_NAME)

def handleMsg(msg):
    if msg is not None or isinstance(msg, dict):
        #TO DO
        task = msg
        
    else:
        print 'Message is broken'
        return




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