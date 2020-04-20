# Running the App

Once you clone this repo or download the files: 
- in Terminal, cd into the app/backend folder
- run `python main.py`
- go to `localhost:5000` to access app

## Debugging
- Make sure to have an Arduino connected to the computer.
  + If you do have an Arduino connected but are getting an error that says `No such file or directory: '/dev/cu.usbmodem...'`:
    - in `serialcomm.py`, change the serial route to the route to your Arduino which can be found using the Arduino IDE
- Make sure to have flask installed on your computer. 

## Frontend 

If any changes to the frontend are made:
- in Terminal, cd into the app/frontend folder
- run `npm run build`
