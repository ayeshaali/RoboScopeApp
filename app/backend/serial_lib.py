import serial
import grid_handling as gh

class Teensy():
    def __init__(self, serial_port='/dev/cu.usbmodem14201', baud_rate=9600,
            read_timeout=5):
        self.conn = serial.Serial(serial_port, baud_rate)
        self.conn.timeout = read_timeout # Timeout for readline()
        self.conn.flushInput()
        self.conn.flushOutput()
    
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
        line_received = self.conn.readline().decode().strip()
        if line_received:   
            vals = line_received.split(';')[:-1]
            for i in range(len(vals)):
                vals[i] = vals[i].split(',')
            print(vals)
            self.conn.flushInput()
            
    def close(self):
        """
        To ensure we are properly closing our connection to the
        Arduino device. 
        """
        self.conn.close()
        print('Connection to Arduino closed')