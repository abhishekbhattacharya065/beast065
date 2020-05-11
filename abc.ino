int mois1;
int mois2;
int fire;
int fire1;
int flag=0;
int flag1=0;
const int trigPin = 12;  
const int echoPin = 10;

long duration;
int distance;

#define BLYNK_PRINT Serial

#include <Servo.h>
#include <ESP8266_Lib.h>
#include <BlynkSimpleShieldEsp8266.h>
Servo myservo;
int pos = 10;
// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "7jU-t0iMMWlo_D-pnVAp_4_GxYVXUIRg";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "ASUS_X00TD";
char pass[] = "abhishek065";

// Software Serial on Uno, Nano...
#include <SoftwareSerial.h>
SoftwareSerial EspSerial(2, 3); // RX, TX

// Your ESP8266 baud rate:
#define ESP8266_BAUD 9600

ESP8266 wifi(&EspSerial);

// Attach virtual serial terminal to Virtual Pin V1
WidgetTerminal terminal(V1);

BLYNK_WRITE(V31)
{
  
  fire=analogRead(A3);
Serial.println(fire);
fire1=fire-22;
Blynk.virtualWrite(V29,fire1);
delay(5);
   if(fire<120)
   {
    digitalWrite(9,LOW);
   }
   if(fire>120) 
   {
    digitalWrite(9,HIGH);
    Blynk.email("abhishek.bhattacharya.15.12.98@gmail.com","FIRE ALERT","IMMEDIETELY CHECK YOUR FIELD");
    Blynk.notify("FIRE ALERT");
   }
  int pinValue = param.asInt(); // assigning incoming value from pin V31 to a variable
  mois1=pinValue;
  // process received value
  mois2 = analogRead(A1);
  mois2=1024-mois2;
  Blynk.virtualWrite(V30,mois2);
   if(mois2>mois1)
   {
    digitalWrite(8,LOW);
    delay(20);
   }
  else 
    {
      digitalWrite(8,HIGH);
      delay(20);
     }
   Blynk.run();
   pinValue=1;
   Blynk.syncVirtual(V31);
}

void setup()
{
  myservo.attach(6);
  pinMode(A3,INPUT);
  pinMode(A1,INPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT);  
  // Debug console
  Serial.begin(9600);

  // Set ESP8266 baud rate
  EspSerial.begin(ESP8266_BAUD);
  delay(10);

  Blynk.begin(auth, wifi, ssid, pass);
  // You can also specify server:
  //Blynk.begin(auth, wifi, ssid, pass, "blynk-cloud.com", 80);
  //Blynk.begin(auth, wifi, ssid, pass, IPAddress(192,168,1,100), 8080);

  // This will print Blynk Software version to the Terminal Widget when
  // your hardware gets connected to Blynk Server
  terminal.println(F("Blynk v" BLYNK_VERSION ": Device started"));
  terminal.println(F("-------------"));
  terminal.println(F("Type 'Marco' and get a reply, or type"));
  terminal.println(F("anything else and get it printed back."));
  terminal.flush();
}


void loop()
{
  Blynk.run();
 //digitalWrite(valve,HIGH); 
  mois2 = analogRead(A1);
  mois2=1024-mois2;
  Blynk.virtualWrite(V30,mois2);
   if(mois2>mois1)
   {
    digitalWrite(8,LOW);
   }
  else 
    {
      digitalWrite(8,HIGH);
     }
//  Serial.println(mois2);  


fire=analogRead(A3);
Serial.println(fire);
fire1=fire-22;
Blynk.virtualWrite(V29,fire1);
delay(5);
   if(fire<120)
   {
    digitalWrite(9,LOW);
   }
   if(fire>120) 
   {
    digitalWrite(9,HIGH);
    Blynk.email("sagarkumarlo647@gmail.com","FIRE ALERT","IMMEDIETELY CHECK YOUR FIELD");
    Blynk.notify("FIRE ALERT");
   }
      
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(20);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
 delay(5);
 
if(distance<25)
{
  flag=flag+1;
  
}

 if(flag1==0)
    flag1=1;
 else if(flag1==1)
    flag1=0;

  if(flag1==0&&flag==1)
    flag=0;

  if(flag>=2)
  {
    digitalWrite(9,HIGH);
    Blynk.email("sagarkumarlo647@gmail.com","ALERT","SOMEONE ENTERED YOUR FIELD");
    Blynk.notify("ALERT");
    flag=0;
    flag1=0;
  }
   

}
