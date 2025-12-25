#include <WiFi.h>

const char* ssid = "SUNBEAM";
const char* password = "1234567890";

void setup() {
  Serial.begin(115200); 
  delay(1000);

  Serial.println("\nConnecting to WiFi network: " + String(ssid));

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected.");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP()); 
}

void loop() {
  // Main program loop (optional, add your main logic here)
  
}
