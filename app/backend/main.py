import flask
import time
import grid_handling
from serialcomm import * 
from threading import Thread
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = flask.Flask("__main__")
socketio = SocketIO(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

thread = None

a = Arduino() 
time.sleep(3)

LED_PIN = 3
BUTTON_PIN = 13
BUTTON_PIN2 = 12
RED = 9;
GREEN = 10;
BLUE = 11;
a.set_pin_mode(LED_PIN,'O')
a.set_pin_mode(BUTTON_PIN,'I')
a.set_pin_mode(BUTTON_PIN2,'I')
a.set_pin_mode(RED,'O')
a.set_pin_mode(GREEN,'O')
a.set_pin_mode(BLUE,'O')

def background_read():
    counter = 0
    while True:
        val = a.digital_read(BUTTON_PIN)
        val2 = a.digital_read(BUTTON_PIN2)
        if val2 == 0:
            grid_handling.toggleactive(1)
            token = grid_handling.get_grid()
            socketio.emit('message', {'data': token})
        if val == 0:
            grid_handling.toggle_module_height(1,1)
            token = grid_handling.get_grid()
            socketio.emit('message', {'data': token})
        time.sleep(0.5)

@app.route("/")
def my_index():
    global thread
    if thread is None:
        socketio.start_background_task(target=background_read)
    token = grid_handling.get_grid()
    return flask.render_template("index.html", token=token)
    
@app.route("/activetoggle", methods=['POST'])
def toggle_active():
    print("thread")
    id = flask.request.args.get("id")
    active = grid_handling.toggleactive(id)
    token = grid_handling.get_grid()
    a.digital_write(LED_PIN, active)
    return flask.render_template("index.html", token=token)
    
@app.route("/module", methods=['POST'])
def toggle_mod_color():
    id = int(flask.request.args.get("id"))
    color = flask.request.args.get("color")
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    grid_handling.toggle_module_color(id,rgb)
    token = grid_handling.get_grid()
    a.analog_write(RED, rgb[0])
    a.analog_write(GREEN, rgb[1])
    a.analog_write(BLUE, rgb[2])
    return flask.render_template("index.html", token=token)

@app.route("/activemodule", methods=['POST'])
def toggle_mod_active():
    id = int(flask.request.args.get("id"))
    grid_handling.toggle_module_active(id, True)
    token = grid_handling.get_grid()
    return flask.render_template("index.html", token=token)

@app.route("/inactivemodule", methods=['POST'])
def toggle_mod_inactive():
    id = int(flask.request.args.get("id"))
    grid_handling.toggle_module_active(id, False)
    token = grid_handling.get_grid()
    return flask.render_template("index.html", token=token)

if __name__ == "__main__":
    socketio.run(app)
