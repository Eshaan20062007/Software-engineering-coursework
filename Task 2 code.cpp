// Task 2 code
// Loovee @ 2015-8-26
#include <math.h>
const int B = 4275000; // B value of the thermistor
const int R0 = 100000; // R0 = 100k
const int pinTempSensor = A0; // Grove - Temperature Sensor connect to A0
const int MAX_READINGS = 180;
float temperatureData[MAX_READINGS]; // Array to store temperature data for 3 minutes
int samplingDelay = 1000; // 1 second delay for sampling
float real[MAX_READINGS];
float imag[MAX_READINGS];
float magnitude[MAX_READINGS];
int currentMode = 0; // 0 = ACTIVE, 1 = IDLE, 2 = POWER_DOWN
float samplingFrequency = 1.0; // 1 sample per second
int amountOfReadings = 180;
float temperatureDifferences[179]; // Array to store temperature differences for 3 minutes

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  collect_temperature_data();
  send_data_to_pc();
  currentMode = decide_power_mode(samplingFrequency);
  apply_power_mode();
} 

void collect_temperature_data(){
    for(int i = 0; i < amountOfReadings; i++){
        int a = analogRead(pinTempSensor);
        float R = 1023.0/a-1.0;
        R = R0*R;
        float temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15;
        temperatureData[i] = temperature;
        delay(samplingDelay);
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
    for (int k = 0; k<amountOfReadings; k++){
      real[k] = 0;
      imag[k] = 0;
      for (int n = 0; n<amountOfReadings; n++){
        real[k] += temperatureData[n] * cos(2*M_PI*k*n/amountOfReadings);
        imag[k] -= temperatureData[n] * sin(2*M_PI*k*n/amountOfReadings);
      }
      magnitude[k] = sqrt(real[k]*real[k] + imag[k]*imag[k]);
    }

    // Calculate frequency using Eq. 3.2
    static float frequency[MAX_READINGS];
    for (int k = 0; k<amountOfReadings; k++){
      frequency[k] = (k * samplingFrequency)/amountOfReadings;
    }
    return frequency;
   }

void send_data_to_pc(){
  float* frequency = apply_dft();
  for (int i = 0; i<amountOfReadings;i++){
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
    if(averageFrequency > 0.5){
        return 0; // ACTIVE
    }
    else if(averageFrequency > 0.1 && averageFrequency <= 0.5){
        return 1; // IDLE
    }
    else{
        return 2; // POWER_DOWN
    }
}

void apply_power_mode(){
    if(currentMode == 0){ // ACTIVE
        amountOfReadings = 180; // set number of readings
        samplingDelay = 1000; // set delay
    }
    else if(currentMode == 1){ // IDLE
        amountOfReadings = 36;
        samplingDelay = 5000;
    }
    else{ // POWER_DOWN
        amountOfReadings = 6;
        samplingDelay = 30000;
    }
}

float calculate_moving_average(){
  for (int i = 1; i<amountOfReadings; i++){
    temperatureDifferences[i-1] = temperatureData[i] - temperatureData[i-1];}

    float sum = 0;
    for (int i = (amountOfReadings-1)-10; i<amountOfReadings-1; i++){
      sum += temperatureDifferences[i];
    }
    return sum/10;
}