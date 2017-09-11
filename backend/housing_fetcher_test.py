import housing_fetcher

def test_basic():
    houses = housing_fetcher.fetch_housing('sfbay','sfc','1500')
    #assert type(houses) is object
    print 'test_basic passed.'
    for result in houses.get_results(sort_by='newest', geotagged=True):
        print result

if __name__ == '__main__':
    test_basic()

