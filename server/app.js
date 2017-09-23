const express = require('express');
const app = express();
const zipData = require('./house_data');

const PORT = process.env.PORT || 8000


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

app.listen(PORT, () => {
    console.log('server is running on port: ' + PORT);
});

