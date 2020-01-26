import cv2
import numpy as np 

image = cv2.imread('..\\MasterOpenCV\\images\\elephant.jpg')
cv2.imshow("original image",image)
cv2.waitKey(0)

# kernel_sharpening = np.array([[-1,-1,-1],
#                               [-1,9,-1],
#                               [-1,-1,-1]])
kernel_sharpening = np.array([[-1,-1],
                              [-1,3]])
sharpened = cv2.filter2D(image,-1,kernel_sharpening)
cv2.imshow("image sharpening ",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()