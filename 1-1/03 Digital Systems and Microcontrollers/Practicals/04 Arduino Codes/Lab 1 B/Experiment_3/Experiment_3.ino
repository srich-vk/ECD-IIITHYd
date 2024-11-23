int inp = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    inp = Serial.read();
    inp = inp - 48;
    //Serial.println(inp);
  }
  if (inp==1) {
    digitalWrite(13, HIGH);
  } else if (inp==0) {
    digitalWrite(13, LOW);
  }
}
