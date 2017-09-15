""" connect to local mongodb """
from pymongo import MongoClient

MONGO_DB_HOST = 'localhost'
MONGO_DB_PORT = '27017'
DB_NAME = 'brkHousing'

CLIENT = MongoClient('%s:%s' % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(database=DB_NAME):
    """ get database by its name """
    return CLIENT[database]




