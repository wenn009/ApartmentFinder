import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App/App';
//import CustomerUpdate from './CustomerUpdate/CustomerUpdate';
import { browserHistory, Router } from 'react-router';
import routes from './routes';
import registerServiceWorker from './registerServiceWorker';
//import 'jquery/dist/jquery.js';
//import 'bootstrap/dist/css/bootstrap.css';
//require('bootstrap/dist/js/bootstrap.min.js');

ReactDOM.render(
  <Router history={browserHistory} routes={routes} />,
  document.getElementById('root')
)
registerServiceWorker();
