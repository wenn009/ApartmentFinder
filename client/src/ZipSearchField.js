import React from 'react';

function ZipSearchField(props) {
  return (
    <div className="container">
      <div className="col-lg-6">
        <div className="input-group">
          <label>Zip Code: </label>
          <input type="text" className="form-control" placeholder="Enter Zip Code" 
                onChange={props.handleChange} value={props.value}></input>
        </div>
      </div>
    </div>
    );
}

export default ZipSearchField;