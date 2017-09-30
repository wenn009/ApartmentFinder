import React from 'react';

function SearchField(props) {
    return (
        <div className="container">
            <div className="col-md-12">
                <form onSubmit={props.handleSearch}>
                    <div className="form-group">
                        <label htmlFor="zip">Zip: </label><br />
                        <input type="text" className="form-control" name="zip"
                            placeholder="Enter a zip code" onChange={props.handleChange}></input>
                        <br />
                        <label htmlFor="price">Select a Price Range: </label>
                        <select className="form-control" onChange={props.handlePrice} name="price">
                            <option value="1">below $1000</option>
                            <option value="2">$1000 ~ $1500</option>
                            <option value="3"> $1500 ~ $2000</option>
                            <option value="4"> $2000 ~ $2500</option>
                            <option value="5" > above $2500</option>
                        </select>
                        <br /><br />
                        <input type="submit" value="Submit" className="btn btn-primary" onClick={props.onSearch}></input>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default SearchField;