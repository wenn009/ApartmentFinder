const express = require('express');
const app = express();
const byZip = require('./house_data');

const PORT = process.env.PORT || 8000

app.get('/', (req,res) => {
    res.json({'hi': 'world'});
})
app.get('/api/v1/:zipCode', (req, res) => {
    const records = byZip[req.params.zipCode];
    if(records === undefined){
  	    res.sendStatus(404);
    }else{
        if(req.query.priceRange === undefined){
            res.json(records);
        }
        res.json({'no':'data'});
    }

});

app.listen(PORT, () => {
    console.log('server is running on port: '+ PORT);
});