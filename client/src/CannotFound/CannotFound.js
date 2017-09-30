import React from 'react';

function CannotFound(props) {
  return (
    <div className="container">
      <div className="alert alert-warning">
        <p>Sorry, we can not find any apartment that matches your needs</p>
      </div>
    </div>);
}

export default CannotFound;