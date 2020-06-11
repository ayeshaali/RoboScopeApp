char operation; // Holds operation (R, W, ...)
char mode; // Holds the mode (D, A)
int pin_number; // Holds the pin number
int digital_value; // Holds the digital value
int analog_value; // Holds the analog value
int value_to_write; // Holds the value that we want to write
int wait_for_transmission = 5; // Delay in ms in order to receive the serial data
int size = 96;

void write_heights(int* data) {
  for (int i=0; i<size; i++) {
    char buf[20];
    sprintf(buf, "%d: %d", i, data[i]);
    Serial.println(buf);
  }
}

void write_colors(int* data) {
  for (int i=0; i<size; i++) {
    char buf[20];
    sprintf(buf, "%d: %d", i, data[i]);
    Serial.println(buf);
  }
}

void setup() {
  Serial.begin(9600); // Serial Port at 9600 baud
  Serial.setTimeout(100); // Instead of the default 1000ms, in order
}

void loop() {
  // Check if characters available in the buffer
  if (Serial.available() > 0) {
    operation = Serial.read();
    delay(wait_for_transmission); // If not delayed, second character is not correctly read
    mode = Serial.read();
    
    int output_values[size] = {0};
    if (Serial.read() == ':') {
      if (operation=='S') {
        size = Serial.parseInt();
      } else {
        char bracket = Serial.read();
        for (int i = 0; i < size; i++) {
          value_to_write = Serial.parseInt();
          output_values[i] = value_to_write;
        }
      }
    }

    switch (operation) {
      case 'W': // Write operation, e.g. WD3:1, WA8:255
        if (mode == 'H') {
          write_heights(output_values);
        } else if (mode == 'C') {
          write_colors(output_values);
        } else {
          break; // Unexpebcted mode
        }
        break;

      case 'R': // Read operation, e.g. RD12, RA4
        if (mode == 'P') { // Digital read
          
        } else {
          break; // Unexpected mode
        }
        break;

      default: // Unexpected char
        break;
    }
  }
}
