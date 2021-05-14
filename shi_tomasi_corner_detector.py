# Shi Tomasi Corner Detector - we an control no of corners to be detucted

import cv2
import numpy as np

img = cv2.imread(r'C:\Users\bhavi\Desktop\Learn_OpenCV\opencv-master\samples\data\pic1.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)  #25 is no of max corner to detect (strong corner)

corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xFF ==27:
    cv2.destroyAllWindow()