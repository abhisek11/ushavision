import cv2
import numpy as np 

image = cv2.imread('..\\MasterOpenCV\\images\\elephant.jpg')
cv2.imshow("original image",image)
cv2.waitKey(0)

#creating our 3X3 kernel
kernel_3X3 = np.ones((3,3),np.float32)/9
blurred = cv2.filter2D(image,-1,kernel_3X3)
cv2.imshow("3X3 blurred image",blurred)
cv2.waitKey(0)

#creating 7X7 kernel 
kernel_7x7 = np.ones((7,7),np.float32)/49
blurred2 = cv2.filter2D(image,-1,kernel_7x7)
cv2.imshow("7X7 blurred image",blurred2)
cv2.waitKey(0)

cv2.destroyAllWindows()
