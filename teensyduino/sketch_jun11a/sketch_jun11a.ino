char operation; // Holds operation (R, W, ...)
char mode; // Holds the mode (D, A)
int pin_number; // Holds the pin number
int digital_value; // Holds the digital value
int analog_value; // Holds the analog value
int value_to_write; // Holds the value that we want to write
int wait_for_transmission = 5; // Delay in ms in order to receive the serial data

struct Pixel { byte node; byte local_id; byte inter; byte height; byte color1; byte color2;};

char* bin(unsigned int k) {
  char* buffer = malloc(8 * sizeof(char)); /* any number higher than sizeof(unsigned int)*bits_per_byte(8) */
  itoa(k, buffer, 2);
  return buffer;
}

void translate_pixels(Pixel buf[], int buf_size) {
  for (int i=0; i<buf_size;i++){
    char str[20];
    sprintf(str, "%d,%d,%s,%d,%X,%X", buf[i].node, buf[i].local_id, bin(buf[i].inter),buf[i].height,buf[i].color1,buf[i].color2);
    Serial.println(str);
  }
}
void send_pixels() {

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

    switch (operation) {
      case 'W': // Write operation, e.g. WD3:1, WA8:255
        int buf_size = Serial.parseInt();
        Pixel buf[buf_size] = {0,0,0,0,0,0};
        
        int j = 0;
        while(Serial.read() !='E') {
          byte temp[5] = {0};
          for (int i =0; i<6;i++) {
            temp[i] = Serial.parseInt();
          }
          buf[j] = {temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]};
          j++;
        }

        translate_pixels(buf, buf_size);
        break;

      case 'R': // Read operation, e.g. RD12, RA4
        send_pixels();
        break;

      default: // Unexpected char
        break;
    }
  }
}
