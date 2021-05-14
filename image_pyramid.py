#Pyramid, or pyramid representation, is a type of multi-scale signal representation in which a signal or an image is subject to repeated smoothing and subsampling.
import cv2
import numpy as np 

img = cv2.imread("lena.jpg")
layer = img.copy()
gp = [layer] #gp = gaussian pyramid

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow('upper level gaussian pyramid',layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)

cv2.imshow("orginal image",img)
cv2.waitKey(0)
cv2.destroyAllWindow()

#Laplacian  & guassian pyramid helps in recontruction of images

#A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid.