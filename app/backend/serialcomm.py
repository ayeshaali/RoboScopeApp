import serial

class Arduino():
    def __init__(self, serial_port='/dev/cu.usbmodem14201', baud_rate=9600,
            read_timeout=5):
        self.conn = serial.Serial(serial_port, baud_rate)
        self.conn.timeout = read_timeout # Timeout for readline()

    def set_pin_mode(self, pin_number, mode):
        """
        Performs a pinMode() operation on pin_number
        Internally sends b'M{mode}{pin_number} where mode could be:
        - I for INPUT
        - O for OUTPUT
        - P for INPUT_PULLUP MO13
        """
        command = (''.join(('M',mode,str(pin_number)))).encode()
        self.conn.write(command)

    def digital_read(self, pin_number):
        command = (''.join(('RD', str(pin_number)))).encode()
        self.conn.write(command)
        line_received = self.conn.readline().decode().strip()
        vals = line_received.split(':') # e.g. D13:1
        if vals[0] == ('D'+ str(pin_number)):
            return int(vals[1])

    def digital_write(self, pin_number, digital_value):
        command = (''.join(('WD', str(pin_number), ':',
            str(digital_value)))).encode()
        self.conn.write(command) 
     
    def analog_read(self, pin_number):
        command = (''.join(('RA', str(pin_number)))).encode()
        self.conn.write(command) 
        line_received = self.conn.readline().decode().strip()
        header, value = line_received.split(':') # e.g. A4:1
        if header == ('A'+ str(pin_number)):
            # If header matches
            return int(value)

    def analog_write(self, pin_number, analog_value):
        command = (''.join(('WA', str(pin_number), ':',
            str(analog_value)))).encode()
        self.conn.write(command) 

    def close(self):
        """
        To ensure we are properly closing our connection to the
        Arduino device. 
        """
        self.conn.close()
        print('Connection to Arduino closed')