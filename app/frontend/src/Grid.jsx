const React = require('react');
const PropTypes = require('prop-types');
const Module = require('./Module');
const css = require('./App.css');
const useState = React.useState;


const Grid = (props) => { 
  let array = props.data.split(')(');
  let mod_array = []
  for (var i=0; i<array.length; i+=8) {
    mod_array.push(array.slice(i,i+8));
  }
  
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
