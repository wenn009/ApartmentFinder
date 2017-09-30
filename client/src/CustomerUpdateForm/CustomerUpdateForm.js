import React from 'react';

function CustomerUpdateForm(props) {
    return (
        <div className="container">
            <div className="col-md-12">
                <form onSubmit={props.handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="name">Name: </label><br />
                        <input type="text" className="form-control" name="name"
                            placeholder="Enter your name" onChange={props.handleChange}></input>
                        <br />
                        <label htmlFor="zipcode">Zip Code: </label><br />
                        <input type="text" className="form-control" name="zipcode"
                            placeholder="e.g 11210" onChange={props.handleChange}></input>
                        <br />
                        <label htmlFor="price_range">Select a Price Range:</label><br />
                        <select className="form-control" onChange={props.handleChange} name="price_range">
                            <option value="1">below $1000</option>
                            <option value="2">$1000 ~ $1500</option>
                            <option value="3"> $1500 ~ $2000</option>
                            <option value="4"> $2000 ~ $2500</option>
                            <option value="5" > above $2500</option>
                        </select>
                        <br />
                        <label htmlFor="near_station">Near Station? </label>
                        <select className="form-control" onChange={props.handleChange} name="near_station">
                            <option value={true}>Yes </option>
                            <option value={false}>No </option>
                        </select>
                        <br />
                        <label htmlFor="telephone">Telephone: </label><br />
                        <input type="text" className="form-control" name="telephone"
                            placeholder="e.g. 6461231234" onChange={props.handleChange}></input>
                        <br />
                        <br /><br />
                        <input type="submit" value="Submit" className="btn btn-primary" onClick={props.onSearch}></input>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default CustomerUpdateForm;