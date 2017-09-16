# fetch housing from craigslist
from craigslist import CraigslistHousing

'''cl_h = CraigslistHousing(site='sfbay', area='sfc', category='roo',
                    filters={'max_price': 1200, 'private_room':True})

for result in cl_h.get_results(sort_by='newest', geotagged=True):
    print result'''
#CraigslistHousing.show_filters()
def fetchHousing(site, area, zip_code):
    houses = CraigslistHousing(site=site, area=area, category='aap', 
                            filters={ 'private_room':True,
                                        'zip_code': zip_code })
    return houses




