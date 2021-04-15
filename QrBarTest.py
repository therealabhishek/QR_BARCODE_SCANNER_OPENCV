
# importing the required libraries:

import cv2
import numpy as np
from pyzbar.pyzbar import decode

image = cv2.imread('1.png')

# printing all the data:
#code = decode(image)
#print(code)

# printing extracts about qrcode:
for qcode in decode(image):
    print(qcode)
    print(qcode.data)
    # decoding the barcode data(which is in bytes):
    myData = qcode.data.decode('utf-8')
    # printing the original message
    print(myData)
    print(qcode.type)

