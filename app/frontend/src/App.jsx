const React = require('react');
const PropTypes = require('prop-types');
const Grid = require('./Grid.jsx');
const useEffect = React.useEffect;
const useState = React.useState;
const css = require('./App.css');
const io = require('socket.io-client');
const socket = io("http://127.0.0.1:5000");

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
      <Grid data={value}/>
    </div>
  );
}

App.propTypes = {
    token: PropTypes.string
};

export default App;
