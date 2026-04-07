// Task 2 code
// Loovee @ 2015-8-26
#include <math.h>
const int B = 4275000; // B value of the thermistor
const int R0 = 100000; // R0 = 100k
const int pinTempSensor = A0; // Grove - Temperature Sensor connect to A0
float temperatureData[180]; // Array to store temperature data for 3 minutes

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  collect_temperature_data();
  print_temperature_data();
}

void collect_temperature_data(){
    for(int i = 0; i<180; i++){
        int a = analogRead(pinTempSensor);
        float R = 1023.0/a-1.0;
        R = R0*R;
        float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15;
        temperatureData[i] = temperature;
        delay(1000);
    }
   }

   //Unit test for collect_temperature_data()
   //Expect: 180 readings stored in temperatureData array
   void print_temperature_data(){
    for(int i = 0; i<180; i++){
        Serial.print("temperature at second ");
        Serial.print(i);
        Serial.print(" = ");
        Serial.println(temperatureData[i]);
    }
   }