from cvzone.SerialModule import SerialObject
from time import sleep
import cv2


arduino = SerialObject()
val1 = 0
val2 = 1

while True:
    arduino.sendData([val1])
    cv2.waitKey(1000)
    arduino.sendData([val2])
    cv2.waitKey(1000)



