String a;

void setup() {

Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
pinMode(5, OUTPUT);
pinMode(6, OUTPUT);
pinMode(7, OUTPUT);
pinMode(8, OUTPUT);
pinMode(9, OUTPUT);

}

void loop() {

a= Serial.readString();// read the incoming data as string
Serial.print(a);

if (a=="a"){
  digitalWrite(9, HIGH);
  delay(500);
  digitalWrite(9, LOW);
}
if (a=="s"){
  digitalWrite(8, HIGH);
  delay(500);
  digitalWrite(8, LOW);
}
if (a=="d"){
  digitalWrite(7, HIGH);
  delay(500);
  digitalWrite(7, LOW);
}
if (a=="f"){
  digitalWrite(6, HIGH);
  delay(500);
  digitalWrite(6, LOW);
}
if (a=="g"){
  digitalWrite(5, HIGH);
  delay(500);
  digitalWrite(5, LOW);
}

}
