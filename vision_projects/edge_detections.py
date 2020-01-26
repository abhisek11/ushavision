import cv2 
import numpy as np 

img = cv2.imread('..\\MasterOpenCV\\images\\input.jpg',0)
cv2.imshow('originl',img)
cv2.waitKey(0)
print(img)
height,width = img.shape

#extract the sobel edges
sobel_x = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobel_y = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)

cv2.imshow("sobel_x",sobel_x)
cv2.waitKey(0)
cv2.imshow("sobel_y",sobel_y)
cv2.waitKey(0)

sobel_or = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("sobel_or",sobel_or)
cv2.waitKey(0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("laplacian",laplacian)
cv2.waitKey(0)

canny = cv2.Canny(img,20,170)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()