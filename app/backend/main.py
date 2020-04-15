import flask
import grid_handling
import serialcomm

app = flask.Flask("__main__")

@app.route("/")
def my_index():
    token = grid_handling.get_grid()
    return flask.render_template("index.html", token=token)
    
@app.route("/activetoggle", methods=['POST'])
def toggle_active():
    id = flask.request.args.get("id")
    grid_handling.toggleactive(id)
    token = grid_handling.get_grid()
    serialcomm.writeArduino("2")
    return flask.render_template("index.html", token=token)
    
app.run(debug=True)