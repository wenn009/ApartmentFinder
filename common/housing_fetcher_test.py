import housing_fetcher

def test_basic():
    houses = housing_fetcher.fetch_housing('newyork','brk','1500', '11214')
    #assert type(houses) is object
    print 'test_basic passed.'
    for result in houses.get_results(sort_by='newest', geotagged=True, limit=5):
        print result

if __name__ == '__main__':
    test_basic()

