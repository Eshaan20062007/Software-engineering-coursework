// Task 2 code
// Loovee @ 2015-8-26
#include <math.h>
const int B = 4275000; // B value of the thermistor
const int R0 = 100000; // R0 = 100k
const int pinTempSensor = A0; // Grove - Temperature Sensor connect to A0
float temperatureData[180]; // Array to store temperature data for 3 minutes
float real[180];
float imag[180];
float magnitude[180];
int currentMode = 0; // 0 = ACTIVE, 1 = IDLE, 2 = POWER_DOWN
float samplingFrequency = 1.0; // 1 sample per second
const int MAX_READINGS = 180;
int amountOfReadings = 180;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  collect_temperature_data();
  print_temperature_data();
  apply_dft();
  send_data_to_pc();
} 

void collect_temperature_data(){
    for(int i = 0; i < amountOfReadings; i++){
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
    for(int i = 0; i<amountOfReadings; i++){
        Serial.print("temperature at second ");
        Serial.print(i);
        Serial.print(" = ");
        Serial.println(temperatureData[i]);
    }
   }

   float* apply_dft(){
    for (int k = 0; k<180; k++){
      real[k] = 0;
      imag[k] = 0;
      for (int n = 0; n<180; n++){
        real[k] += temperatureData[n] * cos(2*M_PI*k*n/180);
        imag[k] -= temperatureData[n] * sin(2*M_PI*k*n/180);
      }
      magnitude[k] = sqrt(real[k]*real[k] + imag[k]*imag[k]);
    }

    // Calculate frequency using Eq. 3.2
    static float frequency[180];
    for (int k = 0; k<180; k++){
      frequency[k] = (k * samplingFrequency)/180;
    }
    return frequency;
   }

void send_data_to_pc(){
  float* frequency = apply_dft();
  for (int i = 0; i<180; i++){
    Serial.print("Time: ");
    Serial.print(i);
    Serial.print(", Temp: ");
    Serial.print(temperatureData[i]);
    Serial.print(", Freq: ");
    Serial.print(frequency[i]);
    Serial.print(", Mag: ");
    Serial.println(magnitude[i]);
  }
}

int decide_power_mode(float averageFrequency){
    if(averageFrequency >){
        return 0; // ACTIVE
    }
    else if(averageFrequency > 1 && averageFrequency <= 0.5){
        return 1; // IDLE
    }
    else{
        return 2; // POWER_DOWN
    }
}