import React, { Component } from 'react';
import 'jquery/dist/jquery.js'
import 'bootstrap/dist/css/bootstrap.min.css';
//import 'bootstrap/dist/js/bootstrap.min.js'
import './App.css';

import City from '../City';
import SearchField from '../SearchField/SearchField';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      zipCode: "",
      cities: []
    }
    this.zipCodeChanged = this.zipCodeChanged.bind(this);
  }

  zipCodeChanged(event) {

    const zip = event.target.value;

    if (zip.length === 5) {
      fetch('http://ctp-zip-api.herokuapp.com/zip/' + zip)
        .then((response) => {
          return response.json();
        })
        .then((jsonBody) => {
          console.log(jsonBody);

          const cityComponents = jsonBody.map((city) => {
            return <City data={city} />
          });

          this.setState({
            cities: cityComponents
          });
        });
    }

    this.setState({
      zipCode: zip
    });
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Find Your Apartment</h2>
        </div>
        <br />
        <SearchField handleChange={this.zipCodeChanged} value={this.state.zipCode} />
        <div>
          {this.state.cities}
        </div>
      </div>
    );
  }
}

export default App;

