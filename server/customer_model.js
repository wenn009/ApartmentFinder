var mongoose = require('mongoose');

var promise = mongoose.connect('mongodb://localhost/customer_infor', {
  useMongoClient: true,
  /* other options */
});

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  // we're connected!
  console.log('Yay! connected to mongo db2');
});

const customerSchema = mongoose.Schema({
    'name': String,
    'telephone': String,
    'zipcode': String,
    'price_range': Number,
    'near_station': Boolean
});


module.exports = mongoose.model('customer', customerSchema);