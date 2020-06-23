char operation; // Holds operation (R, W, ...)
char mode; // Holds the mode (D, A)
int pin_number; // Holds the pin number
int digital_value; // Holds the digital value
int analog_value; // Holds the analog value
int value_to_write; // Holds the value that we want to write
int wait_for_transmission = 5; // Delay in ms in order to receive the serial data

int primary_timer;
int LED =0;

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
  }
  LED=!LED;
  digitalWrite(3, LED);
}

void send_pixels(Pixel buf[], int buf_size) {
  for (int i=0; i<buf_size;i++){
    char str[20];
    sprintf(str, "%d,%d,%s,%d,%X,%X", buf[i].node, buf[i].local_id, bin(buf[i].inter),buf[i].height,buf[i].color1,buf[i].color2);
    Serial.print(str);
    Serial.print(';');
  }
  Serial.println(' ');
}

void setup() {
  Serial.begin(9600); // Serial Port at 9600 baud
  Serial.setTimeout(100); // Instead of the default 1000ms, in order
  pinMode(13, INPUT_PULLUP);
  pinMode(3, OUTPUT);
  primary_timer=millis();
}

void loop() {
  // Check if characters available in the buffer
  if (millis()-primary_timer == 10000) {
    Pixel buffer[2] = {0,0,0,0,0,0};
    send_pixels(buffer,2);
    Serial.println(' ');
    primary_timer=millis();
  }
  
  if (Serial.available() > 0) {
    operation = Serial.read();
    delay(wait_for_transmission);
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
  }
}

void extra() {
  switch (operation) {
    case 'R':
      Pixel buffer[2] = {0,0,0,0,0,0};
      send_pixels(buffer,2);
      break;
    case 'W': 
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
    default: // Unexpected char
      break;
  }
}
