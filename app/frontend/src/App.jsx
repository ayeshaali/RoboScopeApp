const React = require('react');
const PropTypes = require('prop-types');
const Grid = require('./Grid.jsx');
const css = require('./App.css');

const App = (props) => {
  return (
    <div className="App">
      <header className="App-header">
        <p>Welcome</p>
      </header>
      <Grid data={window.token}/>
    </div>
  );
}

App.propTypes = {
    token: PropTypes.string
};

module.exports = App;
