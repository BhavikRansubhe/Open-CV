import cv2
import numpy as np  

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
# To see mouse events like these -> ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 
# 'EVENT_LBUTTONDOWN', 'EVEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']ENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

def click_event(event , x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  #to see color of point clicked on image
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        mycolorImage = np.zeros((512,512,3), np.uint8)
        mycolorImage[:] = [blue,green,red]
        cv2.imshow('color', mycolorImage)

#img = np.zeros( (512,512,3) , np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()





#1. To show Co-ordinates
#  if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,',',y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strXY = str(x) + ', '+ str(y)
#         cv2.putText(img,strXY , (x,y) , font , 1 , (255,255,0),2)
#         cv2.imshow('image',img)


# 2. To give point and then drav a line
# if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img, (x,y), 3, (0,0,255), -1)
#         points.append((x,y))
#         if len(points) >=2:
#             cv2.line(img ,points[-1], points[-2], (255,0,0), 5)
#         cv2.imshow('image',img)