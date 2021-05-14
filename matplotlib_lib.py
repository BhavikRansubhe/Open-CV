import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('lena.jpg',-1)
cv2.imshow('image',img)
img  = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #bcoz matplotlib uses RGB


plt.imshow(img)
plt.xticks([]),plt.yticks([]) #to hide x and y coordinats in fig
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()