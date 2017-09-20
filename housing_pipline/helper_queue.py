import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloud_amqp_client import CloudAMQPClient

SCRAPE_HOUSING_QUEUE_URL = 'amqp://tebodcbi:SaF4IwTvyZIm6HlRQuMu0gV0jdbOnLBJ@rhino.rmq.cloudamqp.com/tebodcbi'
SCRAPE_HOUSING_QUEUE_NAME = 'houses_scrape_queue'


def clearQueue(queue_url, queue_name):
    scrape_news_queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.get_message()
            if msg is None:
                print "Cleared %d messages." % num_of_messages
                return
            num_of_messages += 1

    print 'num of messages cleared: %d' % num_of_messages


if __name__ == "__main__":
    clearQueue(SCRAPE_HOUSING_QUEUE_URL, SCRAPE_HOUSING_QUEUE_NAME)
