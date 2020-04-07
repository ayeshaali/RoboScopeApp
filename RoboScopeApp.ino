int incomingData;

void setup() {
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
  pinMode(11,INPUT_PULLUP);
  pinMode(13,OUTPUT);
}

void loop() {
  if (Serial.available()) {
    incomingData = Serial.read();
    if (incomingData == '1') {
      digitalWrite(13, HIGH);
      Serial.write("LED Turned ON");
    }
    if (incomingData == '0') {
      digitalWrite(13, LOW);
      Serial.write("LED Turned OFF");
    }
  }

  int val = digitalRead(11);
  if (val){
    digitalWrite(13, LOW);
    Serial.println("LED Turned OFF");
  }else{ 
    digitalWrite(13, HIGH);
    Serial.println("LED Turned ON");
  }

}
