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
a.set_pin_mode(LED_PIN,'O')
a.set_pin_mode(BUTTON_PIN,'I')

def background_read():
    counter = 0
    while True:
        val = a.digital_read(BUTTON_PIN)
        if val == 0:
            print(val)
            grid_handling.toggleactive(1)
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

if __name__ == "__main__":
    socketio.run(app)
