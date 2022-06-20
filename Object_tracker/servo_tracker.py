import cv2
import numpy as np
from PCA9685 import PCA9685

servo_max_angle = 180
servo_min_angle = 0
position = 90  # center position of servo

pwm = PCA9685(0x40, debug=False)
pwm.serFreq(50)
# put servo motor at start position
pwm.setServoPosition(0, position)  # 0 is servo0

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# cap.set(3, 480) # REduce screen size if servo and processor is lagging
# cap.set(4, 320)
rows, cols, width = frame.shape
x_med = int(cols / 2)
center = x_med
while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BRG2HSV)
    high_red = np.array([161, 155, 84])
    low_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    _, contours, _ = cv2.findContours(red_mask, cv2.RETE_TREE, cv2.CHAIN_APROX_SIMPLE)
    contours = sorted(x, key=lambda x: cv2.contourArea(x), reverse=True)
    for ctr in contours:
        (x, y, w, h) = cv2.boundingRect(ctr)
        rect_colour = (0, 255, 0)
        # cv2.rectangle(frame, (x, y), (x+w, y+h), rect_colour, 2)
        # Get medium of target rect
        x_med = int((x + x + w) / 2)
        # get a line thru the middle of the target object
        break
    cv2.line(frame, (x_med, 0), (x_med, 480), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    # Move servo
    if x_med < center - 30:
        position += 1
    elif x_med > center + 30:
        position -= 1
    pwm.setServoPosition(0, position)


cap.release()
cv2.destroyAllWindows()
