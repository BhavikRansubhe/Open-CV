import cv2

img = cv2.imread('lena.jpg',-1) #reading image
cv2.imshow('image',img)  #to show image in window
k = cv2.waitKey(5000)

if k == 27: #esc
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img) #to make a copy of image
    cv2.destroyAllWindows()












