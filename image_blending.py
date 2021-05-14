import cv2
import numpy as np 

apple = cv2.imread(r'C:\Users\bhavi\Desktop\Learn_OpenCV\opencv-master\samples\data\apple.jpg')
orange = cv2.imread(r'C:\Users\bhavi\Desktop\Learn_OpenCV\opencv-master\samples\data\orange.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:,:256],orange[:,256:]))#it takes apple half left side and orange half right side

#generate gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#generate gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# genearate laplacian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_expanded)
    lp_apple.append(laplacian)

# genearate laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_expanded)
    lp_orange.append(laplacian)

  # now add left and right halvs of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap , orange_lap in zip (lp_apple,lp_orange):
    n+=1
    cols, rows , ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(cols/2)], orange_lap[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

#now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)


cv2.imshow("apple",apple)
cv2.imshow("orange",orange)
cv2.imshow("apple_orange",apple_orange)
cv2.imshow("apple_orange_reconstruct",apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindow()



#STEPS:
#1. Load the two images of apple and orange. 
# 2. Find the Gaussian Pyramids for apple and orange (in this particular example, number of levels is 6). 
# 3. From Gaussian Pyramids, find their Laplacian Pyramids. 
# 4. Now join the left half of apple and right half of orange in each levels of Laplacian Pyramids. 
# 5. Finally from this joint image pyramids, reconstruct the original image.




