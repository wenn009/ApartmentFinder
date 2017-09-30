import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import 'jquery/dist/jquery.js';
import 'bootstrap/dist/css/bootstrap.css';

const Base = ({ children }) => (
    <div>
        <nav className="navbar navbar-default">
            <div className="container-fluid">
                <div className="navbar-header">
                    <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                        <span className="sr-only">Toggle navigation</span>
                        <span className="icon-bar"></span>
                        <span className="icon-bar"></span>
                        <span className="icon-bar"></span>
                    </button>
                    <a className="navbar-brand" href="#">Apartment Finder</a>
                </div>


                <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">


                    <ul className="nav navbar-nav navbar-right">
                        <li><Link to='/'>Search Apartment</Link></li>
                        <li><Link to='/subscribe'>Subscribe for Update</Link></li>

                    </ul>
                </div>
            </div>
        </nav>


        <br />
        {children}
    </div>
);

Base.propTypes = {
    children: PropTypes.object.isRequired
};

export default Base;