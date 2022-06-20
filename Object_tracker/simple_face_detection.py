import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
# using media pipe package on CVzone wrapper

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    cv2.imshow("image", img)
    cv2.waitKey(1)


