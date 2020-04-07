import serial
ser = serial.Serial('/dev/cu.usbmodem14201')
ser.flushInput()

def readArduino():
    ser_bytes = ser.readline()
    decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
    print(decoded_bytes)

def writeArduino(towrite):
    ser.write(str.encode(towrite))
