const customerModel = require('./customer_model');
const c = new customerModel();

const addCustomer = function (body) {
    return new Promise((resolve, reject) => {

        c.name = body.name;
        c.telephone = body.telephone;
        c.zipcode = body.zipcode;
        c.price_range = body.price_range;
        c.near_station = body.near_station;

        c.save((err) => {
            if (err) {
                reject(err);
            }
            resolve({ message: "created!" });

        });
    });
}

const deleteCustomer = function (telephone) {
    console.log("hey?");
    return new Promise((resolve, reject) => {
        c.findOne(
            {"telephone": telephone}, 
            {"_id": true},
            (err, c) => {
            if(err) reject(err);
            console.log(c);
            resolve({message: "deleted!"});
        });
    });


}

module.exports = { addCustomer, deleteCustomer};