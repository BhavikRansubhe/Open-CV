import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt 

img = cv.imread('gradient.png',0)
_, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
_, th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
#in binary their is either 0 or 1 , if pixel values less than 127 then its 0 i.e its black .
_, th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)  #in TRUNV value after 127 will remain same
_, th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)  #in TOZERO value before 127 will remain 0 only
_, th5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Orignal Img','BINARY' ,'BINARY_INV','TRUNC' , 'TOZERO','TOZERO_INV']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) #to hide x and y coordinats in fig

plt.show()

# cv.imshow("Image",img)
# cv.imshow("th1",th1)
# cv.imshow("th3",th3)
# cv.imshow("th4",th4)

# cv.waitKey(0)
# cv.destroyAllWindow()