import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('ascii')
        print(myData)
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(img, [points], True, (255, 150, 63), 5)
        #print data on the live pictures
        points2 = barcode.rect
        cv2.putText(img, myData,(points2[0], points2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 100, 218), 2)
        


    cv2.imshow('result', img)
    cv2.waitKey(1)