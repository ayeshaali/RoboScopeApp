const React = require('react');
const PropTypes = require('prop-types');
const MaterialPicker = require('react-color')['MaterialPicker'];
const css = require('./App.css');
const useState= require('react')['useState'];

// modules
const options = [
  { value: '0', label: ' ' },
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
  // parse token (grid string) in the same way as in Grid component
  let array = props.data.split(')(');
  let mod_array = []
  for (var i=0; i<array.length; i+=8) {
    mod_array.push(array.slice(i,i+8));
  }
  
  // states for forms:  
  let [modState, setModState] = useState('0'); //which module selected
  let [controlState, setControlState] = useState(false); //if module selected controlState is true
  let [colorState, setColorState] = useState('#2196F3'); //if controlState true, colorState allows to determine which color has been selected
  
  // handle change to module select
  const handleChange = (selectedOption) => {
    setModState(selectedOption); //sets modState to new module value
    if (selectedOption!=null) {
      setControlState(true); //sets controlState to true
    }
  };

  let control_select = null
  if (controlState==true) { //will show control options for module
    //get module values and first square that is active
    let selected_mod = mod_array[modState-1]; 
    let first_square = null;
    for (var i =0; i <selected_mod.length; i++) {
      first_square = selected_mod[0].split(",");
      if (first_square[1]==1) {
        break;
      }
    }
    
    // all control options: MaterialPicker (color selector), active/inactive toggles, height
    control_select = (
      <div className="module-control">
        <MaterialPicker color={ colorState }
          onChangeComplete={e=> setColorState(e.hex) }/>
        <form action={'/module?id='+(modState)+'&color='+((colorState).toString().slice(1))} method="post">
          <button type="submit" name="submitButton">Submit</button>
        </form>
        
        <form action={'/activemodule?id='+(modState)} method="post">
          <button type="submit" name="submitButton">Toggle Active</button>
        </form>
        
        <form action={'/inactivemodule?id='+(modState)} method="post">
          <button type="submit" name="submitButton">Toggle Inactive</button>
        </form>
        
        <form action={'/inactivemodule?id='+(modState)} method="post">
          <label for="height">Height</label>
          <input type="text" id="height" name="height" value = {first_square[5]}/>
        </form>
      </div>
    );
  }

  return (
    <div className="control-panel">
      <h1> Controls </h1>
      <select id="lang" onChange={e=> handleChange(e.target.value)} value={modState}>
        {options.map((option)=> {
          return <option value={option.value}>{option.label}</option>
        })}
      </select>
      {control_select}
    </div>
    
  );
};

ControlPanel.propTypes = {
};

export default ControlPanel;
