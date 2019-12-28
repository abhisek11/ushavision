import cv2 
import numpy as np 

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg')
image = cv2.resize(img,(960,540))

M= np.ones(image.shape,dtype="uint8")*75

added = cv2.add(image,M)
cv2.imshow("added ",added)

subtracted = cv2.subtract(image,M)
cv2.imshow("subtracted",subtracted)

cv2.waitKey()
cv2.destroyAllWindows()