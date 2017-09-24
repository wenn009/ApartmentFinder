import React from 'react';

function City(props) {
  return (
    <div className="container">
      <div className="panel panel-primary">
        <div className="panel-heading">
         {props.data.City}
        </div>
        <div className="panel-body">
          <ul>
            <li>State: {props.data.State}</li>
            <li>EstimatedPopulation: {props.data.EstimatedPopulation}</li>
          </ul>
        </div>
      </div>
    </div>);
}

export default City;
