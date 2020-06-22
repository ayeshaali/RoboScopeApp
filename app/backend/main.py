import flask
import time
import grid_handling
from serial_lib import *
from threading import Thread
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = flask.Flask("__main__")
socketio = SocketIO(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

thread = None #hold background thread to read from arduino pins

t = Teensy()
time.sleep(3)

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
    t.write_pixels([0,1,2,3,4])
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
