import React from 'react';

function House(props) {
  return (
    <div className="container">
      <div className="panel panel-primary">
        <div className="panel-heading">
         {props.data["name"]}
        </div>
        
            <div className="panel-body">
            <a href={props.data["url"]}>
            <img src={props.data["image_url"]} alt="Smiley face" height="100" width="100"/>
            <span> {props.data["price"]}</span> <br />
            <span>{props.data["where"]}</span>
            </a>
           </div>
        
        
      </div>
    </div>);
}

export default House;