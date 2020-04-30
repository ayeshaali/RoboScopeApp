const React = require('react');
const PropTypes = require('prop-types');
const css = require('./App.css');

// turn RGB colors into hex value
const componentToHex= (c)=> {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

const rgbToHex = (r, g, b)=> {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

const GridSquare = (props) => {
  // determines active status (two classes in App.css: .active or .inactive)
  let active = parseInt(props.properties[1])==1 ? "active": "inactive";
  // set hex value for the background color of the grid GridSquare
  //    if active use color, if inactive use default inactive color
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
