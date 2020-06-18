import serial
import grid_handling as gh

class Teensy():
    def __init__(self, serial_port='/dev/cu.usbmodem14201', baud_rate=9600,
            read_timeout=5):
        self.conn = serial.Serial(serial_port, baud_rate)
        self.conn.timeout = read_timeout # Timeout for readline()
    
    def write_pixels(self, list):
        """
        Performs a digital read on pin_number and returns the value (1 or 0)
        Internally sends b'RD{pin_number}' over the serial connection
        """
        val = gh.serial_get(list)
        self.conn.write("W".encode())
        self.conn.write(str(len(list)).encode())
        command=""
        separator = ','
        for pixel in val:
            command+="P"
            command+=separator.join(pixel)
        self.conn.write(command.encode()) 
        self.conn.write("E".encode())
    
    def read_pixels(self):
        """
        Performs a read from Serial for urban pixel information and returns the value (1 or 0)
        Internally sends b'RD' over the serial connection
        """
        command = ('RP').encode()
        self.conn.write(command)
        line_received = self.conn.readline().decode().strip()
        vals = line_received.split(':')
        if vals[0] == ('D'+ str(pin_number)):
            return int(vals[1])
            
    def close(self):
        """
        To ensure we are properly closing our connection to the
        Arduino device. 
        """
        self.conn.close()
        print('Connection to Arduino closed')