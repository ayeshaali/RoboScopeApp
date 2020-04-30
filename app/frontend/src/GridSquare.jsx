const React = require('react');
const PropTypes = require('prop-types');
const css = require('./App.css');

const componentToHex= (c)=> {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

const rgbToHex = (r, g, b)=> {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

const GridSquare = (props) => {
  let active = parseInt(props.properties[1])==1 ? "active": "inactive";
  let hex=null;
  if (active=="active") {
    hex = rgbToHex(parseInt(props.properties[2]),parseInt(props.properties[3]),parseInt(props.properties[4]));
    console.log(hex);
  }
  return (
    <div className={'grid-item ' + active} style={{background: hex}}>
      <form action={'/activetoggle?id=' + (props.properties[0].replace("(",""))} method="post">
         <button type="submit" name="submitButton">{props.properties[0].replace("(", "")}</button>
       </form>
    </div>
  );
}

GridSquare.propTypes = {
  
};

module.exports = GridSquare;
