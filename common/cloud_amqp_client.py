""" This module demonstrates documentation of cloud AMQP Client

Example:
        $ python cloud_amqp.py

Attributes:
    send_message: sends a message to cloud AMQP
    get_message: received a message from cloud AMQP """

import json
import pika

class CloudAMQPClient(object):
    """ define cloud AMQP class """
    def __init__(self, cloudamqp_url, queue_name):
        """ initial connection with cloud amqp """
        self.cloudamqpurl = cloudamqp_url
        self.queue_name = queue_name
        self.params = pika.URLParameters(cloudamqp_url)
        self.params.socke_time_timeout = 3
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, message):
        """ send a message to queue """
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=json.dumps(message))
        print '[x] Sent message to %s: %s' % (self.queue_name, message)

    def get_message(self):
        """ receive a message from queue """
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name) # pylint: disable = unused-variable
        if method_frame:
            print '[x] Received message from %s: %s' % (self.queue_name, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return json.loads(body)
        else:
            print 'No message get from %s' % self.queue_name
            return None

    def sleep(self, seconds):
        """ BlockingConnetion.sleep() is a safer way to sleep than time.sleep() """
        self.connection.sleep(seconds)
