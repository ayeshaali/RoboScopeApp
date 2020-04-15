const React = require('react');
const PropTypes = require('prop-types');
const GridSquare = require('./GridSquare');
const css = require('./App.css');

const Grid = (props) => { 
  let array = props.data.split(')(');
  
  
  const gridsquares = array.map((square) => {
      let square_arr = square.split(",");
      return (<GridSquare properties={square_arr} />);
  });

  return (
    <div className="grid-container">
      {gridsquares}
    </div>
  );
}

Grid.propTypes = {
};

module.exports = Grid;
