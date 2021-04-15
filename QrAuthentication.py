# importing the required libraries:
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# initializing the camera
cap = cv2.VideoCapture(0)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)

# reading data from textfile:
with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()

while True:
    ret, frame = cap.read()

    for qrcode in decode(frame):
        # print(qrcode.data)
        # print(qrcode.type)
        myData = qrcode.data.decode('utf-8')
        print(myData)

        # checking authorization:

        if myData in myDataList:
            myOutput = 'Authorized'
            myColor =  (0, 255, 0)
            #print('Authorized')
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)
            #print('Unauthorized')

        pts1 = np.array([qrcode.polygon], np.int32)
        pts1 = pts1.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts1], True, myColor, 5)

        pts2 = qrcode.rect
        cv2.putText(frame, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)

    cv2.imshow('Result', frame)
    cv2.waitKey(1)