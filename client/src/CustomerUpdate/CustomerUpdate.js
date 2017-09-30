import React, { Component } from 'react';
import CustomerUpdateForm from '../CustomerUpdateForm/CustomerUpdateForm';

class CustomerUpdate extends Component {
    constructor() {
        super();
        this.state = {
            customer: {
                name: "",
                near_station: true,
                zipcode: "",
                price_range: 1,
                telephone: ""
            },
            feedback: ""

        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleChange(event) {
        const fieldName = event.target.name;
        const customer = this.state.customer;
        customer[fieldName] = event.target.value;
        this.setState({ customer });
    }

    handleSubmit(event) {
        console.log('The zip code was submitted: ' + this.state.customer.zipcode);
        console.log('The price was submitted: ' + this.state.customer.price_range);
        console.log('The name was submitted: ' + this.state.customer.name);
        console.log('The telephone was submitted: ' + this.state.customer.telephone);
        console.log('The is near station was submitted: ' + this.state.customer.near_station);
        event.preventDefault();
        const zip = this.state.customer.zipcode;
        const price = this.state.customer.priceRange;
        const name = this.state.customer.name;
        const telephone = "+1" + this.state.customer.telephone;
        const isNearStation = this.state.customer.near_station;

        if (zip.length === 5) {
            fetch('http://localhost:8000/api/v1/customer_information', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    zipcode: zip,
                    price_range: price,
                    name: name,
                    telephone: telephone,
                    near_station: isNearStation
                })
            })
                .then((response) => {
                    return response.json();
                })
                .then((jsonBody) => {
                    this.setState({ feedback: "Success! We will notify once we find any apartment that matches your needs" })
                });
        }
    }


    render() {
        return (
            <div>
                <div className="container">
                    <h1> Subscribe to recieve update </h1>
                </div>
                <br />
                <CustomerUpdateForm handleChange={this.handleChange}
                    handleSubmit={this.handleSubmit}
                    value={this.state.zipcode} />
                <br /> <br />
                <div className="container">
                    <div className="col-md-12">
                        {this.state.feedback.length !== 0
                            && <div className="alert alert-success" role="alert">
                                <p>{this.state.feedback}</p>
                            </div>
                        }
                    </div>
                </div>


            </div>
        );
    }
}

export default CustomerUpdate;
