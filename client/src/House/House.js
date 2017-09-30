import React from 'react';
import './House.css';

function House(props) {
  return (
        <div className="col-sm-12 col-md-4">
          <div className="thumbnail">
            <img src={props.data["image_url"]} alt="image" className="image-responsive" />
            <div className="caption">
              <h3>{props.data["where"]}</h3>
              <p>{props.data["name"]}</p>
              <p>{props.data["price"]}   
              <span className="pull-right label label-info">
                {props.data["bedrooms"]} bedrooms </span>
              </p>
              {props.data["nearStation"] === true && <span className="pull-right label label-success">station near by</span>}
              {props.data["nearStation"] === false && <span className="pull-right label label-warning">not near station</span>}
              <p><a href={props.data["url"]} className="btn btn-primary" role="button">View Detail</a></p>
            </div>
          </div>
        </div>
  )
}

export default House;
