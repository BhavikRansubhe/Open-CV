# In camshift window size can be changed automatic , which was not happening in meanshift method 

import cv2
import numpy as np 

cap = cv2.VideoCapture('car_traffic.mp4')

#take first frame of the video
ret , frame = cap.read()

#set up intial location of window
x,y,width,height = 280,330,100,60
track_window = (x,y,width,height)

#set the region of interest roi for tracking
roi = frame[y:y+height,x:x+width]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((0.,60.,32.)), np.array((180.,255.,255)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

#setup the termination criteria,either 10 iteration or move by atleast 1 point
term_crict= ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT , 10, 1)
cv2.imshow('roi',roi)

while(1):
    ret , frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(720,480),fx=0,fy=0, interpolation = cv2.INTER_CUBIC) #resize video step 3
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        #apply meanshift to get the new loaction
        ret, track_window =cv2.CamShift(dst,track_window,term_crict)   
        #Draw it on image
        pts = cv2.boxPoints(ret)
        print(pts)
        pts = np.int0(pts)
        final_image = cv2.polylines(frame,[pts],True,(0,255,0),2)

        # x,y,w,h = track_window
        # final_image = cv2.rectangle(frame,(x,y),(x+w,y+h),255,3)
        
        cv2.imshow('final image',final_image)
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break
    else:
        break

# cap.release()
# out.release()
# cv2.destroyAllWindows()