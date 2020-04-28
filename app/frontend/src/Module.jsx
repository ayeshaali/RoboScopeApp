const React = require('react');
const PropTypes = require('prop-types');
const GridSquare = require('./GridSquare');
const css = require('./App.css');

const Module = (props) => { 
  let array = props.properties;
  
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
