const HousingModel = require('./house_model');

const byZip = {};

HousingModel.find({}, function(err, houses){
    if(err){
        console.log(err);
    }else{
        //console.log(houses.length);
        houses.map((house) => {
            if(byZip[house['zipcode']] === undefined){
                byZip[house['zipcode']] = [];
            }
            byZip[house['zipcode']].push(house);
        });
    }
});

module.exports = byZip;


