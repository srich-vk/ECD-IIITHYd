int digin = 0; 

void setup() {
  Serial.begin(9600);
  pinMode(13, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digin = digitalRead(13);
  //Serial.println(digin);
  if (digin){
    Serial.println("Hello World");
  } else {
    Serial.println("Bye World");
  }
  //delay(500);
}
