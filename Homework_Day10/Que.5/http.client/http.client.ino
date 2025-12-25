#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "vivo Y27";
const char* password = "12345678";


const char* serverURL = "http://10.82.203.75:4000/soil_moisture1"; 


#define SOIL_PIN 34
#define SENSOR_ID "ESP32_01"

void setup() {
  Serial.begin(115200);
  delay(1000);

  pinMode(SOIL_PIN, INPUT);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {

    int adcValue = analogRead(SOIL_PIN);   // 0 – 4095
    int moisture = map(adcValue, 0, 4095, 100, 0);

    Serial.print("ADC Value: ");
    Serial.print(adcValue);
    Serial.print("  Moisture: ");
    Serial.print(moisture);
    Serial.println("%");

    HTTPClient http;
    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{";
    jsonData += "\"sensor_id\":\"" SENSOR_ID "\",";
    jsonData += "\"moisture_level\":" + String(moisture);
    jsonData += "}";

    int httpResponseCode = http.POST(jsonData);

    Serial.print("HTTP Response Code: ");
    Serial.println(httpResponseCode);

    http.end();
  } 
  else {
    Serial.println("WiFi Disconnected");
  }

  delay(5000);  
}


