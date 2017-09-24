import React from 'react';

function SearchField(props) {
    return (
        <div className="container">
            <div className="col-md-12">
                <form>
                    <div className="form-group">
                        <label for="zip">Zip: </label>
                        <input type="text" className="form-control" name="zip"
                                placeholder="Enter Zip Code"></input>
                        <label for="price">Price: </label>
                        <input type="text" className="form-control" name="price"
                                placeholder="Enter Price Range"></input>
                    </div>
                    <button type="submit" className="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    );
}

export default SearchField;