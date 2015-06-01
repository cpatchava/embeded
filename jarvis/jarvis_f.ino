#include <codes.h>

String readString;

int led = 13;
int led_light = 12;
int curr_fan = 0;
int curr_tv = 0;
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(led_light, OUTPUT);
}

void loop(){ 

  while ( Serial.available() )
  { 
    delay( 3 );
    char c = Serial.read();
    readString += c;
  }


  if ( readString.length() >0 ) {
    Serial.println( readString );
    if(readString == "Jarvis fan on" && !(curr_fan)){
      fan_on_off();
      digitalWrite(led_light, HIGH);
      curr_fan = 1;
      Serial.println("fan on");
    }
    else if(readString == "Jarvis fan off" && curr_fan){
      fan_on_off();
      digitalWrite(led_light, LOW);
      curr_fan = 0;
      Serial.println("fan off"); 
    }
    else if(readString == "Jarvis fan speed increase"){
      fan_speed();
      Serial.println("fan speed increase"); 
       }
    else if(readString == "Jarvis fan speed decrease"){
      fan_speed();
      delayMicroseconds(1600 );
      fan_speed();
      Serial.println("decrease"); 
    }
    else if(readString == "Jarvis tv on" && !curr_tv){
      tv_remote_on_off();
      Serial.println("tv on"); 
      curr_tv = 1;
    }
    else if(readString == "Jarvis tv off" && curr_tv){
      tv_remote_on_off();
      Serial.println("tv off"); 
      curr_tv = 0;
    }
    else if(readString == "Jarvis mute"){
      tv_remote_mute();
      Serial.println("tv mute"); 
      
    }
    readString="";
  }
  
}
