""" test mongodb_client module """
import mongodb_client as client

def test_basic():
    """ test mongodb by adding and dropping database """
    database = client.get_db('test')
    database.testCollection.drop()
    assert database.testCollection.count() == 0
    database.testCollection.insert({'test': 0, 'hello':'world'})
    assert database.testCollection.count() == 1
    database.testCollection.drop()
    assert database.testCollection.count() == 0
    print 'test_basic passed.'

if __name__ == '__main__':
    test_basic()

