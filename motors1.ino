#include <ros.h>
#include <Servo.h>
#include <ros.h>
#define USE_STM32_HW_SERIAL 
void setup() {
int lfront = 3;
int rfront = 4;
}

void setup() {
  Serial.begin(9600); //revise/check
  pinMode(lfront, OUTPUT);
  pinMode(rfront, OUTPUT);
}

void loop() {
  //go forward
  analogWrite(3, 75); //motor pin, SPEED
  analogWrite(4, 75); //motor pin, SPEED
  delay(2);

  //go backward
  analogWrite(3, -75); //motor pin, SPEED
  analogWrite(4, -75); //motor pin, SPEED
  delay(2);

}void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
