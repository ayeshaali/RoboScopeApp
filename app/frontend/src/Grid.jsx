const React = require('react');
const PropTypes = require('prop-types');
const Module = require('./Module');
const css = require('./App.css');
const useState = React.useState;

// main component on page: contains entire grid
const Grid = (props) => {
  // parse through grid string (token)
  // split into grid squares
  let array = props.data.split(')(');
  // split into modules
  let mod_array = []
  for (var i=0; i<array.length; i+=8) {
    mod_array.push(array.slice(i,i+8));
  }
  
  // create modules 
  const modules = mod_array.map((mod) => {
      return (<Module properties={mod} />);
  });

  return (
    <div className="grid-container">
      {modules}
    </div>
  );
}

Grid.propTypes = {
};

module.exports = Grid;
