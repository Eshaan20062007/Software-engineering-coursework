#include <math.h>
const int B = 4275000;
const int R0 = 100000;
const int pinTempSensor = A0;
int readingCount = 0; // counts how many readings have been taken

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if(readingCount < 180){ // stop after 180 readings (3 minutes)
    int a = analogRead(pinTempSensor);
    float R = 1023.0/a-1.0;
    R = R0*R;
    float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15;
    Serial.print("time: ");
    Serial.print(readingCount);
    Serial.print(", temperature: ");
    Serial.println(temperature);
    readingCount++;
    delay(1000);
  }
}