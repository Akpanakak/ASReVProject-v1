from cvzone.SerialModule import SerialObject

arduino = SerialObject() # finds arduino by default

while True:
    my_data = arduino.getData()
    print(my_data)
    # This is a false change

"""
// ON Arduino

#include <cvzone.h>
SerialData serialData;
int sendVals[2}; // value of min 2 even when sending 1

void setup(){
serialData.Begin(9600);

}

void loop(){
int potVal = analogRead(A0);
sendVal[0] = potVal; // Store val in the array before sending all vals
serialData.Send(sendVal);
}
"""
