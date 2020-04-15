import * as serviceWorker from './serviceWorker';

const React = require('react');
const ReactDOM = require('react-dom');
const PropTypes = require('prop-types');
const App = require('./App'); 
const css_index = require('./index.css');

ReactDOM.render(
  <App />,
  document.getElementById('root')
);

serviceWorker.unregister();
