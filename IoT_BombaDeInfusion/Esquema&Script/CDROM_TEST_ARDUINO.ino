const int pin_A1=10;
const int pin_A2=11;
const int pin_ENA=5;

const int pin_B1=12;
const int pin_B2=13;
const int pin_ENB=6;

const int speed=30;
const int a=1;
void setup() {
pinMode(pin_A1,OUTPUT);
pinMode(pin_A2,OUTPUT);
pinMode(pin_ENA,OUTPUT);

pinMode(pin_B1,OUTPUT);
pinMode(pin_B2,OUTPUT);
pinMode(pin_ENB,OUTPUT);

// start serial port at 9600 bps:
Serial.begin(9600);

while (!Serial) {
; // wait for serial port to connect. Needed for native USB port only
}

}
void loop() {
if(a==1){
run_forward();
}
else{
run_backward();  
} 
}
void run_forward(){
  digitalWrite(pin_ENA,1);
  digitalWrite(pin_A1,1);
  digitalWrite(pin_A2,0);
  digitalWrite(pin_ENB,0);
  digitalWrite(pin_B1,0);
  digitalWrite(pin_B2,0);
  delay(speed);
  digitalWrite(pin_ENA,0);
  digitalWrite(pin_A1,0);
  digitalWrite(pin_A2,0);
  digitalWrite(pin_ENB,1);
  digitalWrite(pin_B1,1);
  digitalWrite(pin_B2,0);
  delay(speed);
  digitalWrite(pin_ENA,1);
  digitalWrite(pin_A1,0);
  digitalWrite(pin_A2,1);
  digitalWrite(pin_ENB,0);
  digitalWrite(pin_B1,0);
  digitalWrite(pin_B2,0);
  delay(speed);
  digitalWrite(pin_ENA,0);
  digitalWrite(pin_A1,0);
  digitalWrite(pin_A2,0);
  digitalWrite(pin_ENB,1);
  digitalWrite(pin_B1,0);
  digitalWrite(pin_B2,1);
  delay(speed);
}
void run_backward()
{
  digitalWrite(pin_ENA,0);
  digitalWrite(pin_A1,0);
  digitalWrite(pin_A2,0);
  digitalWrite(pin_ENB,1);
  digitalWrite(pin_B1,1);
  digitalWrite(pin_B2,0);
  delay(speed);
  digitalWrite(pin_ENA,1);
  digitalWrite(pin_A1,1);
  digitalWrite(pin_A2,0);
  digitalWrite(pin_ENB,0);
  digitalWrite(pin_B1,0);
  digitalWrite(pin_B2,0);
  delay(speed);
  digitalWrite(pin_ENA,0);
  digitalWrite(pin_A1,0);
  digitalWrite(pin_A2,0);
  digitalWrite(pin_ENB,1);
  digitalWrite(pin_B1,0);
  digitalWrite(pin_B2,1);
  delay(speed);
  digitalWrite(pin_ENA,1);
  digitalWrite(pin_A1,0);
  digitalWrite(pin_A2,1);
  digitalWrite(pin_ENB,0);
  digitalWrite(pin_B1,0);
  digitalWrite(pin_B2,0);
  delay(speed);
}
