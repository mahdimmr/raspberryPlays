#include "ESP8266WiFi.h"
#include <PubSubClient.h>


const int TRIG_PIN = 13;
const int ECHO_PIN = 15;
const int blue = 12;
const int green = 14;
const int red = 16;
const char* ssid = "\\  -_-  /";
const char* password = "M76m1414";

WiFiClient wifiClient;
PubSubClient client(wifiClient);

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i=0;i<length;i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("clinetid")) {
      Serial.println("connected");
      client.publish("hello","hello from esp");
      client.subscribe("hello");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println("try again in 5 seconds");
      delay(5000);
    }
  }
}

void distanceDo(long distanceCm, long distanceIn) {
  if (distanceCm <= 0){
    Serial.println("Out of range");
  } else {
    Serial.print(distanceIn);
    Serial.print("in: ");
    Serial.print(distanceCm);
    Serial.print("cm");
    Serial.println();
  };
  if (distanceCm >= 13) {
    digitalWrite(red, LOW);
    digitalWrite(blue, LOW);
    digitalWrite(green, HIGH);
  }
  else if ( 6 <= distanceCm && distanceCm <= 12){
    digitalWrite(red, LOW);
    digitalWrite(blue, HIGH);
    digitalWrite(green, LOW);
  }
  else {
    digitalWrite(red, HIGH);
    digitalWrite(blue, LOW);
    digitalWrite(green, LOW);
  };
  
  char *str = (char*)malloc(13 * sizeof(char));;
  sprintf(str, "%ld cm", distanceCm);
  client.publish("helloitsme", str);
  char *str2 = (char*)malloc(13 * sizeof(char));;
  sprintf(str2, "%ld inch", distanceIn);
  client.publish("helloitsme", str2);
}


void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(ECHO_PIN,INPUT);
  client.setServer("192.168.1.41", 1883);
  client.setCallback(callback);  
  
  Serial.print(WiFi.localIP());
  Serial.println("");
  Serial.println("WiFi connection Successful");
  Serial.print("The IP Address of ESP8266 Module is: ");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) 
  {
     delay(500);
     Serial.print("*");
  }
}
 
void loop()
{
  long duration, distanceCm, distanceIn;
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);
  distanceCm = duration / 29.1 / 2 ;
  distanceIn = duration / 74 / 2;
  distanceDo(distanceCm, distanceIn);
  
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
}
