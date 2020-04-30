const React = require('react');
const PropTypes = require('prop-types');
const Grid = require('./Grid.jsx');
const ControlPanel = require('./ControlPanel.jsx').default;
const useEffect = require('react')['useEffect'];
const useState = require('react')['useState'];
const css = require('./App.css');
const socket = require('socket.io-client')("http://127.0.0.1:5000");

const App = (props) => {
  const [value, setValue] = useState(window.token);
  
  socket.on('connect', function() {
      console.log('Websocket connected!');
  });
  
  useEffect(() => {
    socket.on('message', function(msg) {
      console.log("arduino");
      setValue(msg.data);
    });
  }, [value]);

  
  return (
    <div className="App">
      <header className="App-header">
        <p>Welcome</p>
      </header>
      <div className="app-container">
      <Grid data={value}/>
      <ControlPanel data={value}/>
      </div>
    </div>
  );
}

App.propTypes = {
    token: PropTypes.string
};

export default App;
