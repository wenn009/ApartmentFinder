const HousingModel = require('./house_model');

const byZip = {};

HousingModel.find({}, function (err, houses) {
    if (err) {
        console.log(err);
    } else {
        //console.log(houses.length);
        houses.map((house) => {
            if (byZip[house['zipcode']] === undefined) {
                byZip[house['zipcode']] = [];
            }
            byZip[house['zipcode']].push(house);
        });
    }
});

const getHousesByPrice = function (rangeNumber, houses) {
    return new Promise((resolve, reject) => {
        const PRICE_RANGE_MAP = {
            1: 1000,
            2: 1500,
            3: 2000,
            4: 2500,
            5: 3000
        }
        const houseDataByPrice = [];
        houses.map((house) => {
            HOUSE_PRICE_STRING = house['price']
            HOUSE_PRICE = parseInt(HOUSE_PRICE_STRING.substring(1)); //remove '$'
            if (HOUSE_PRICE < PRICE_RANGE_MAP[rangeNumber]
                && HOUSE_PRICE > PRICE_RANGE_MAP[rangeNumber] - 1000) {
                houseDataByPrice.push(house);
            }
        });
        resolve(houseDataByPrice);
    });
}

module.exports = { byZip, getHousesByPrice };
