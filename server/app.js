const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();
const zipData = require('./house_data');
const customerData = require('./customer_handler');
//const router = express.Router();

const PORT = process.env.PORT || 8000
//allow cross origin
app.use(cors());
//configure app using boday parser so data from POST request can be used
app.use(bodyParser.urlencoded({ extended: true}));
app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.json({ 'hi': 'world' });
})
app.get('/api/v1/:zipCode', (req, res) => {
    const records = zipData.byZip[req.params.zipCode];
    if (records === undefined) {
        res.sendStatus(404);
    }
    if (req.query.priceRange === undefined) {
        res.json(records);
    } else {
        const rangeNumber = req.query.priceRange;
        zipData.getHousesByPrice(+rangeNumber, records)
            .then(houses => res.json(houses));
    }
});

app.post('/api/v1/customer_information', (req, res)=>{
    customerData.addCustomer(req.body)
        .then(message => res.json(message));
});

app.delete('/api/v1/customer_information/:telephone', (req, res)=>{
    console.log(req.params.telephone);
    customerData.deleteCustomer(req.params.telephone)
        .then(message => res.json(message));
});

app.listen(PORT, () => {
    console.log('server is running on port: ' + PORT);
});

