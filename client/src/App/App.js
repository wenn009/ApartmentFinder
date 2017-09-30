import React, { Component } from 'react';
import './App.css';

import House from '../House/House';
import SearchField from '../SearchField/SearchField';
import CannotFoud from '../CannotFound/CannotFound';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      zipCode: "",
      houses: [],
      priceRange: "1"
    }
    this.handleSearch = this.handleSearch.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handlePrice = this.handlePrice.bind(this);
  }

  handleChange(event) {
    let zip;
    if (event.target.value.length >= 5) {
      zip = event.target.value;
      this.setState({ zipCode: zip });
    }

  }

  handlePrice(event) {
    this.setState({ priceRange: event.target.value });
  }


  handleSearch(event) {
    console.log('The zip code was submitted: ' + this.state.zipCode);
    console.log('The selection was: ' + this.state.priceRange);
    event.preventDefault();
    const zip = this.state.zipCode;
    const price = "?priceRange=" + this.state.priceRange;

    if (zip.length === 5) {
      fetch('http://localhost:8000/api/v1/' + zip + price)
        .then((response) => {
          return response.json();
        })
        .then((jsonBody) => {
          console.log(jsonBody);

          const houses = jsonBody.map((house, idx) => {
            return <House data={house} key={idx} />
          });

          if (houses.length === 0) {
            houses.push(<CannotFoud />);
          }

          this.setState({
            houses
          });
        });
    }

    this.setState({
      zipCode: zip
    });
  }

  render() {
    return (
      <div>
        <SearchField handleChange={this.handleChange} handleSearch={this.handleSearch} handlePrice={this.handlePrice} value={this.state.zipCode} />
        <div className="container">
          <div className="row">
            {this.state.houses}
          </div>
        </div>
      </div>
    );
  }
}

export default App;

