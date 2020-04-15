from flask import Flask, request
import project 
import serialcomm 

app = Flask(__name__)

@app.route("/")
def home():
    return '''<!DOCTYPE html>
    <html>
    <body>
      <form action="/LED" method="post">
        <button type="submit" name="submitButton" value="Toggle">Toggle LED</button>
      </form>
    </body>
    </html>'''

@app.route("/LED", methods=['GET', 'POST'])
def change():
    serialcomm.writeArduino('2')
    return '''<!DOCTYPE html>
    <html>
    <body>
      <form action="/LED" method="post">
        <button type="submit" name="submitButton" value="Toggle">Toggle LED</button>
      </form>
    </body>
    </html>'''
    
    
if __name__ == "__main__":
    app.run(debug=True)