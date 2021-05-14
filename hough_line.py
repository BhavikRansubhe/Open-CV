#The Hough Transform is a popular technique to detect any shape, if you can represent that shape in a mathematical form. It can detect the shape even if it is broken or distorted a little bit.

#Hough transformation Algorithm 
# 1. Edge detection, e.g. using the Canny edge detector. 
# 2. Mapping of edge points to the Hough space and storage in an accumulator. 
# 3. Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by thresholding and possibly other constraints. 
# 4. Conversion of infinite lines to finite lines.

#OpenCV implements two kind of Hough Line Transforms The Standard Hough Transform (HoughLines method) The Probabilistic Hough Line Transform (HoughLinesP method)

import cv2
import numpy as np 

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize=3) #50 & 150 are thresold values
lines = cv2.HoughLines(edges,1,np.pi/180,200)
#image :  source image. 
# lines :Output vector of lines. Each line is represented by a 2 or 3 element vector (p, theta) or (p, theta, votes) p is the distance from the coordinate origin ( (0, 0) (top-left corner of the image). 8 is the line rotation angle in radians. votes is the value of accumulator. 
#  rho: Distance resolution of the accumulator in pixels. 
# theta: Angle resolution of the accumulator in radians. 
# threshold (>threshold) Accumulator threshold parameter. Only those lines are returned that get enough votes

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho

    # x1 stores the rounded off value off value of (r * cos(theta) -1000 * sin(theta))
    x1 = int(x0 + 1000 *(-b))
    # y1 stores the rounded off value off value of (r * sin(theta) +1000 * cos(theta))
    y1 = int(y0 + 1000 *(a))
    # x2 stores the rounded off value off value of (r * cos(theta) +1000 * sin(theta))
    x2 = int(x0 - 1000 *(-b))
    # y2 stores the rounded off value off value of (r * sin(theta) -1000 * cos(theta))
    y2 = int(y0 - 1000 *(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('image',img)
k =cv2.waitKey(0)
cv2.destroyAllWindow()


