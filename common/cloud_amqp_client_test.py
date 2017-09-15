""" to test cloud_amqp_client module """
from cloud_amqp_client import CloudAMQPClient

CLOUDAMQP_URL = 'amqp://fnalqjaj:HHhdNuH0oH3HjQIrrv8KekTPIlLFyG7y@wombat.rmq.cloudamqp.com/fnalqjaj'
TEST_QUEUE_NAME = 'test'


def test_basic():
    """ test if sent message equals the received message """
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)
    send_msg = {'test': 'ans'}
    client.send_message(send_msg)
    received_msg = client.get_message()
    assert send_msg == received_msg
    print 'test_basic() passed'


if __name__ == '__main__':
    test_basic()
