#define START 0  //example definition
#define DOWN 1  //example definition
#define UP 2

int down_initial;
int up_initial;
const int BUTTON_TIMEOUT = 150; //button timeout in milliseconds
bool LED = 0;
bool prev_LED = 0;
int state = 0;

void setup() {
  Serial.begin(9600); // set the baud rate
  pinMode(11,INPUT_PULLUP);
  pinMode(13,OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {
  number_fsm(digitalRead(11));
}


void number_fsm(uint8_t input){
  switch(state){
    case START: 
      if (Serial.available()) {
        int incomingData = Serial.read();
        if (incomingData == '2') {
          LED=!LED;
        }
      }

      if (LED!=prev_LED) {
        digitalWrite(13, LED);
        prev_LED=LED;
      }
      
      if (input==0){
        down_initial = millis();
        state = DOWN;
      }
      
      break;
    case DOWN:
      if ((millis()-down_initial)< BUTTON_TIMEOUT) {
        if (millis()-down_initial > 20 && input==1) {
          up_initial = millis();
          state = UP;
        }
      } else {
        state = START;
      }
      break;
    case UP:
      if ((millis()-up_initial)< BUTTON_TIMEOUT) {
        if (millis()-up_initial > 20 && input==0) {
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
