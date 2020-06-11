import serial
import grid_handling as gh

class Teensy():
    def __init__(self, serial_port='/dev/cu.usbmodem14201', baud_rate=9600,
            read_timeout=5):
        self.conn = serial.Serial(serial_port, baud_rate)
        self.conn.timeout = read_timeout # Timeout for readline()
    
    def set_size(self, pixel_num):
        """
        Sends height array from db
        Internally sends b'WH:{list} where mode could be:
        """
        command = (''.join(('SS:',str(pixel_num)))).encode()
        self.conn.write(command)
        
    def write_heights(self):
        """
        Sends height array from db
        Internally sends b'WH:{list} where mode could be:
        """
        heights = gh.get_all_heights()
        command = (''.join(('WH:',str(heights)))).encode()
        self.conn.write(command)
    
    def write_colors(self):
        """
        Sends color array from db
        Internally sends b'WC:{list} where mode could be:
        """
        colors = gh.get_all_colors()
        command = (''.join(('WC:',str(colors)))).encode()
        self.conn.write(command)
    
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