#An image gradient is a directional change in the intensity or color in an image
import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

img=cv2.imread ("messi5.jpg", cv2.IMREAD_GRAYSCALE) 
#img=cv2.imread ("sudoku.png", cv2.IMREAD_GRAYSCALE) 


lap=cv2.Laplacian(img, cv2.CV_64F, ksize=3) 
lap =np.uint8(np.absolute(lap)) 
sobelX =cv2.Sobel (img, cv2.CV_64F, 1 ,0) #more change in intensity in x diretion
sobelY =cv2.Sobel (img, cv2.CV_64F, 0,1) # change  in y direction
edges = cv2.Canny(img,100,200) 


sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCOmbined = cv2.bitwise_or(sobelX,sobelY)


titles=['prime imag ', 'Laplacian','sobelX','sobelY','sobelCOmbined','edges'] 
images=[img, lap,sobelX,sobelY,sobelCOmbined,edges] 
for i in range (6):
    plt.subplot (2, 3, i + 1) ,plt. imshow (images [i], 'gray')
    plt.title (titles[i]) 
    plt.xticks ([]),plt.yticks ([]) 
    
plt.show()