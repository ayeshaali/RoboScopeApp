import flask
import time
import grid_handling
from serialcomm import * 
from serial_lib import *
from threading import Thread
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = flask.Flask("__main__")
socketio = SocketIO(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

thread = None #hold background thread to read from arduino pins

a = Arduino()  #create arduino
t = Teensy()
time.sleep(3)

#current arduino system: two buttons (pins 12, 13), one RGB LED (pins 9,10,11), one LED (pin 3)
LED_PIN = 3
BUTTON_PIN = 13
BUTTON_PIN2 = 12
RED = 9
GREEN = 10
BLUE = 11
# a.set_pin_mode(LED_PIN,'O')
# a.set_pin_mode(BUTTON_PIN,'I')
# a.set_pin_mode(BUTTON_PIN2,'I')
# a.set_pin_mode(RED,'O')
# a.set_pin_mode(GREEN,'O')
# a.set_pin_mode(BLUE,'O')

def background_read():
    counter = 0
    while True:
        # read from both buttons
        # val = a.digital_read(BUTTON_PIN2) 
        # if val == 0: 
        #     #button one for toggling active/inactive status of a square (set to 1)
        #     grid_handling.toggleactive(1)
        #     token = grid_handling.get_grid()
        #     socketio.emit('message', {'data': token}) #send grid to web app to rerender
        
        # val2 = a.digital_read(BUTTON_PIN)
        # if val2 == 0: 
        #     #button two for increasing height (increment by 1) of a module (set to 1)
        #     grid_handling.toggle_module_height(1,1)
        #     token = grid_handling.get_grid()
        #     socketio.emit('message', {'data': token}) #send grid to web app to rerender
        time.sleep(0.5)

@app.route("/")
def my_index():
    # start app
    global thread
    if thread is None:
        socketio.start_background_task(target=background_read)
    token = grid_handling.get_grid()
    return flask.render_template("index.html", token=token)
    
@app.route("/activetoggle", methods=['POST'])
def toggle_active():
    # arguments: id of grid square (id: int)
    # function: will change active status of square
    print("thread")
    id = flask.request.args.get("id")
    #grid changes and resultant grid
    active = grid_handling.toggle_active(id)
    token = grid_handling.get_grid()
    #arduino write
    t.write_pixels([1,2,3,4,5])
    # a.digital_write(LED_PIN, active)
    return flask.render_template("index.html", token=token)
    
@app.route("/module", methods=['POST'])
def toggle_mod_color():
    # arguments: id of module (id: int), color to set module to (color: hex)
    # function: change color of all squares in module
    #           light up RGB LED on arduino with request color
    id = int(flask.request.args.get("id"))
    color = flask.request.args.get("color")
    #RGB conversion
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4)) 
    #grid changes and resultant grid
    grid_handling.toggle_module_color(id,rgb)
    token = grid_handling.get_grid()
    #arduino write
    # a.analog_write(RED, rgb[0])
    # a.analog_write(GREEN, rgb[1])
    # a.analog_write(BLUE, rgb[2])
    return flask.render_template("index.html", token=token)

@app.route("/activemodule", methods=['POST'])
def toggle_mod_active():
    # arguments: id of module (id: int)
    # function: make all squares active
    id = int(flask.request.args.get("id"))
    #grid changes and resultant grid
    grid_handling.toggle_module_active(id, True)
    token = grid_handling.get_grid()
    return flask.render_template("index.html", token=token)

@app.route("/inactivemodule", methods=['POST'])
def toggle_mod_inactive():
    # arguments: id of module (id: int)
    # function: make all squares inactive
    id = int(flask.request.args.get("id"))
    #grid changes and resultant grid
    grid_handling.toggle_module_active(id, False)
    token = grid_handling.get_grid()
    return flask.render_template("index.html", token=token)

if __name__ == "__main__":
    socketio.run(app)
