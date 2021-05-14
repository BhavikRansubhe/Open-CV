import cv2
import numpy as np 

cap = cv2.VideoCapture(r'C:\Users\bhavi\Desktop\Learn_OpenCV\opencv-master\samples\data\vtest.avi')
# fgbg = cv2.createBackgroundSubtractorMOG2() #to detect shadow
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True) #defaukt is true only


while True:
    ret,frame = cap.read()

    if frame is None:
        break
    fgmask = fgbg.apply(frame)

    cv2.imshow("Frame",frame)
    cv2.imshow("FG MASK Frame",fgmask)

    keyboard = cv2.waitKey(30)

    if keyboard == 27:
        break


cv2.destroyAllWindow()
cap.release()