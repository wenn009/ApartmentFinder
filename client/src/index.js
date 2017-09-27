import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App/App';
import registerServiceWorker from './registerServiceWorker';
import 'jquery/dist/jquery.js';
import 'bootstrap/dist/css/bootstrap.css';
//require('bootstrap/dist/js/bootstrap.min.js');

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
