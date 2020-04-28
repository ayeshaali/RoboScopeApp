const React = require('react');
const Select = require('react-select');
const PropTypes = require('prop-types');
const css = require('./App.css');
const useState= require('react')['useState'];

const options = [
  { value: '1', label: 'Module 1' },
  { value: '2', label: 'Module 2' },
  { value: '3', label: 'Module 3' },
  { value: '4', label: 'Module 4' },
  { value: '5', label: 'Module 5' },
  { value: '6', label: 'Module 6' },
  { value: '7', label: 'Module 7' },
  { value: '8', label: 'Module 8' },
  { value: '9', label: 'Module 9' },
  { value: '10', label: 'Module 10' },
  { value: '11', label: 'Module 11' },
  { value: '12', label: 'Module 12' }
];

const ControlPanel = (props) => { 
  let [state, setState] = useState("Module 1");

  return (
    <div className="control-panel">
    
    </div>
  );
};

ControlPanel.propTypes = {
};

module.exports= ControlPanel;
