import numpy as np  
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # no of rows and channnel
print(img.size) # no of pixels
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340 , 330:390] #add same ball to another pos
img[273:333 , 100:160] = ball

img =cv2.resize(img,(512,512)) # images need to be of same size to add
img2 =cv2.resize(img2,(512,512))
#dst = cv2.add(img, img2);
dst = cv2.addWeighted(img, .8 , img2 , .2 , 0);


cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindow()
