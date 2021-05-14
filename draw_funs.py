import cv2

# import numpy as np
# img  = np.zeros([512,512,3],np.uint8) ... for black background

img = cv2.imread('lena.jpg',1) #reading image

img = cv2.line(img , (0,0) , (255,255) , (0,0,255) ,5)
img = cv2.arrowedLine(img , (0,255) , (255,255) , (0,255,0) ,2)
# arguments 2&3 are cordinates 
# 4 is color scheme B G R fromat for red it is (0,0,255) google rbg color picker for more color
# 5 is thickness size

img = cv2.rectangle(img , (384,0) , (510,128) , (0,0,255) ,5) #if we provide thickess as -1 it will fill the shape

img = cv2.circle(img , (447,63) , 63 , (255,0,0) ,-1) # 2 nd argu is centre and 3rd is radius

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', ( 10,500) , font , 4 ,(255,255,255), 10 , cv2.LINE_AA)
#2 is text to write , 3 is where , 4 is szie and last is line type


cv2.imshow('image',img)  #to show image in window

cv2.waitKey(5000)

cv2.destroyAllWindows()