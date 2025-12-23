#define MQ2_PIN 34 
#define LED_PIN 12 

void setup() {
  Serial.begin(115200); 
  pinMode(MQ2_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("MQ-2 Gas Sensor Test");
}

void loop() {
  int sensorValue = analogRead(MQ2_PIN); 
  Serial.print("Sensor Value: ");
  Serial.println(sensorValue);

  if (sensorValue > 1000) 
  { 
    digitalWrite(LED_PIN, HIGH); 
  } 
  else
   {
    digitalWrite(LED_PIN, LOW);  
  }

  delay(1000); 
}
