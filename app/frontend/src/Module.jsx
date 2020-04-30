const React = require('react');
const PropTypes = require('prop-types');
const GridSquare = require('./GridSquare');
const css = require('./App.css');

// creates module of 8 squares: directed to from Grid component
const Module = (props) => { 
  let array = props.properties;
  
  // create gridsquares using array of 8 squares
  const gridsquares = array.map((square) => {
      let square_arr = square.split(",");
      return (<GridSquare properties={square_arr} />);
  });

  return (
    <div className="module-container">
      {gridsquares}
    </div>
  );
}

Module.propTypes = {
};

module.exports = Module;
