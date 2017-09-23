var mongoose = require('mongoose');

var promise = mongoose.connect('mongodb://localhost/brkHousing', {
  useMongoClient: true,
  /* other options */
});

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  // we're connected!
  console.log('Yay! connected to mongo db');
});

const HousingSchema = mongoose.Schema({
    'name': String,
    'area': String,
    'url': String,
    'has_map': Boolean,
    'price': String,
    'bedrooms': Number,
    'zipcode': Number,
    'geotag': Array,
    'nearStation': Boolean,
    'image_url': String,
    'has_image': Boolean,
    'datetime': Date,
    'where': String,
    'id': Number
});


/*
{u'name': u'ALL ORIGINAL DETAIL___EXPOSED BRICK___CEILINGS FANS___ROOF DECK___', 
u'area': None, 
u'url': u'https://newyork.craigslist.org/brk/abo/d/all-original-detailexposed/6312947322.html', 
u'has_map': True, 
u'price': u'$2300', 
u'bedrooms': u'2', 
u'zipcode': u'11216', 
u'geotag': [40.687245, -73.954684], 
'nearStation': True, 
'image_url': 'https://maps.googleapis.com/maps/api/streetview?fov=90&pitch=0&key=AIzaSyCkpVrJULDUUBqQEVd_pqK6lIpAkcsQ8Bs&size=400x400&location=40.687245,-73.954684', 
u'has_image': True, 
u'datetime': u'2017-09-19 20:09', 
u'where': u'BED-STUY___G TRAIN @ CLASSON AVE___', 
u'id': u'6312947322'}*/

const HousingModel = mongoose.model('houses', HousingSchema);
/*let data = new HousingModel({
  "name" : "HUGE FURNISHED BACKYARD__CENTRAL AIR__LAUNDRY__TONS OF BIG WINDOWS__",
	"area" : null,
	"url" : "https://newyork.craigslist.org/brk/abo/d/huge-furnished/6312947371.html",
	"has_map" : true,
	"price" : "$2600",
	"bedrooms" : "3",
	"zipcode" : "11207",
	"geotag" : [
		40.684086,
		-73.908629
	],
	"nearStation" : true,
	"image_url" : "https://maps.googleapis.com/maps/api/streetview?fov=90&pitch=0&key=AIzaSyCkpVrJULDUUBqQEVd_pqK6lIpAkcsQ8Bs&size=400x400&location=40.684086,-73.908629",
	"has_image" : true,
	"datetime" : "2017-09-19 20:42",
	"where" : "BUSHWICK___J/Z TRAINS @ CHAUNCEY AVE___",
	"id" : "6312947371"
});
data.save();*/

module.exports = HousingModel;
