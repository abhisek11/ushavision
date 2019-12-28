import cv2
import numpy as np  

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg')
image = cv2.resize(img,(960,540))
smaller  = cv2.pyrDown(image)
large = cv2.pyrUp(smaller)

cv2.imshow("original",image)
cv2.imshow("smaller",smaller)
cv2.imshow("large",large)

cv2.waitKey()
cv2.destroyAllWindows()