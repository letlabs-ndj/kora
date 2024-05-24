
#define BLYNK_PRINT Serial

/* Fill in information from Blynk Device Info here */
#define BLYNK_TEMPLATE_ID "TMPL2lb-CJlua"
#define BLYNK_TEMPLATE_NAME "test"
#define BLYNK_AUTH_TOKEN "zaJLroZ66sM9fnPyW77UN3h753VOH4i3" 
 
#define BLYNK_PRINT Serial
#define DHTPIN 25
#define DHTTYPE DHT11
 

// const double k = 5.0/1024;
// const double luxFactor = 500000;
// const double R2 = 10000;
// const double LowLightLimit = 200; 
// const double B = 1.25*pow(10.0,7);
// const double m = -1.4;

int const LED = 27;
int const VEN = 12;
int sensorVal;


#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include "DHT.h"
 
char auth[] = BLYNK_AUTH_TOKEN;
 
// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "Airbox-A949";
char pass[] = "14602665";

DHT dht(DHTPIN, DHTTYPE); // constructor to declare our sensor
BlynkTimer timer; 
float t, h,l;
 
BLYNK_WRITE(V0)
{
  int pinValue=param.asInt();
  if (pinValue == 1) {
    digitalWrite(LED, HIGH); // Turn on the fan
  } else {
    digitalWrite(LED, LOW);  // Turn off the fan
  }
}
BLYNK_WRITE(V1)
{
  int pinValue=param.asInt();
  if (pinValue == 1) {
    digitalWrite(VEN, HIGH); // Turn on the fan
  } else {
    digitalWrite(VEN, LOW);  // Turn off the fan
  }
}

void sendData()
{
  h = dht.readHumidity();
  t = dht.readTemperature();  
  l = calcLightIntensity();
  Blynk.virtualWrite(V2, t);
  Blynk.virtualWrite(V3, h);
  Blynk.virtualWrite(V4, l);
}

float calcLightIntensity()
{
    int ldrValue = analogRead(36);  // Read LDR value
    float voltage = (5.0 / 1023.0) * ldrValue;  // Convert the analog value to voltage
    float lux = 50.0 - (250.0 / voltage);
    Serial.print("luminosite : ");
    Serial.print(lux);
    Serial.print("\n");
    return lux;
}

void setup()
{
  pinMode(LED,OUTPUT);
  pinMode(VEN,OUTPUT);
  // Debug console
  Serial.begin(9600);
  dht.begin();
 
  Blynk.begin(auth, ssid, pass);
  delay(2000); 
  timer.setInterval(1000L, sendData); 
 
}
 
void loop()
{
  analogReadResolution(12);
  Blynk.run();
  timer.run(); // Initiates SimpleTimer
}