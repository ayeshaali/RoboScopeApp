const React = require('react');
const PropTypes = require('prop-types');
const css = require('./App.css');

const GridSquare = (props) => {
  return (
    <div className={'grid-item ' + (parseInt(props.properties[1])==1 ? "active": "inactive")}>
      <form action={'/activetoggle?id=' + (props.properties[0])} method="post">
         <button type="submit" name="submitButton">{props.properties[0]}</button>
       </form>
    </div>
  );
}

GridSquare.propTypes = {
  
};

module.exports = GridSquare;
