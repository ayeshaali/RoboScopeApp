#define START 0  //example definition
#define DOWN 1  //example definition
#define UP 2

int down_initial;
int up_initial;
const int BUTTON_TIMEOUT = 150; //button timeout in milliseconds
bool LED = 0;
bool prev_LED = 0;
int state = 0;

char operation; // Holds operation (R, W, ...)
char mode; // Holds the mode (D, A)
int pin_number; // Holds the pin number
int digital_value; // Holds the digital value
int analog_value; // Holds the analog value
int value_to_write; // Holds the value that we want to write
int wait_for_transmission = 5; // Delay in ms in order to receive the serial data

const uint32_t red = 0; //hardware pwm channel used in secon part
const uint32_t green = 1;
const uint32_t blue = 2;

void set_pin_mode(int pin_number, char mode) {
  switch (mode) {
    case 'I':
      pinMode(pin_number, INPUT);
      break;
    case 'O':
      pinMode(pin_number, OUTPUT);
      break;
    case 'P':
      pinMode(pin_number, INPUT_PULLUP);
      break;
  }
}

void digital_read(int pin_number) {
  digital_value = digitalRead(pin_number);
  Serial.print('D');
  Serial.print(pin_number);
  Serial.print(':');
  Serial.println(digital_value); // Adds a trailing \n
}

void analog_read(int pin_number) {
  analog_value = analogRead(pin_number);
  Serial.print('A');
  Serial.print(pin_number);
  Serial.print(':');
  Serial.println(analog_value); // Adds a trailing \n
}

void digital_write(int pin_number, int digital_value) {
  digitalWrite(pin_number, digital_value);
}

void analog_write(int pin_number, int analog_value) {
  analogWrite(pin_number, analog_value);
  Serial.println(pin_number);
  Serial.println(analog_value);
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
    pin_number = Serial.parseInt(); // Waits for an int to be transmitted
    if (Serial.read() == ':') {
      value_to_write = Serial.parseInt(); // Collects the value to be written
    }
    switch (operation) {
      case 'R': // Read operation, e.g. RD12, RA4
        if (mode == 'D') { // Digital read
          digital_read(pin_number);
        } else if (mode == 'A') { // Analog read
          analog_read(pin_number);
        } else {
          break; // Unexpected mode
        }
        break;

      case 'W': // Write operation, e.g. WD3:1, WA8:255
        if (mode == 'D') { // Digital write
          digital_write(pin_number, value_to_write);
        } else if (mode == 'A') { // Analog write
          analog_write(pin_number, value_to_write);
        } else {
          break; // Unexpected mode
        }
        break;

      case 'M': // Pin mode, e.g. MI3, MO3, MP3
        set_pin_mode(pin_number, mode); // Mode contains I, O or P (INPUT, OUTPUT or PULLUP_INPUT)
        break;

      default: // Unexpected char
        break;
    }
  }
}

void number_fsm(uint8_t input) {
  switch (state) {
    case START:
      if (Serial.available()) {
        int incomingData = Serial.read();
        if (incomingData == '2') {
          LED = !LED;
        }
      }

      if (LED != prev_LED) {
        Serial.println(LED);
        digitalWrite(13, LED);
        prev_LED = LED;
      }

      if (input == 0) {
        down_initial = millis();
        state = DOWN;
      }

      break;
    case DOWN:
      if ((millis() - down_initial) < BUTTON_TIMEOUT) {
        if (millis() - down_initial > 20 && input == 1) {
          up_initial = millis();
          state = UP;
        }
      } else {
        state = START;
      }
      break;
    case UP:
      if ((millis() - up_initial) < BUTTON_TIMEOUT) {
        if (millis() - up_initial > 20 && input == 0) {
          down_initial = millis();
          state = DOWN;
        }
      } else {
        state = START;
        LED = !LED;
      }
      break;
  }
}
