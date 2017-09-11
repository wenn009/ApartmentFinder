# fetch housing from craigslist
from craigslist import CraigslistHousing

'''cl_h = CraigslistHousing(site='sfbay', area='sfc', category='roo',
                    filters={'max_price': 1200, 'private_room':True})

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    print result'''

def fetch_housing(site, area, max_price):
    houses = CraigslistHousing(site=site, area=area, category='roo', 
                            filters={'max_price': max_price, 'private_room':True})
    return houses
