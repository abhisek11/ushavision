import cv2
import numpy as np  

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg')
image_scaled = cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow("scalling -Linear Interpolation",image_scaled)
cv2.waitKey()

image_scaled = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("scalling -Cubic Interpolation",image_scaled)
cv2.waitKey()

image_scaled = cv2.resize(img,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow("scalling -SKEWED SIZE Interpolation",image_scaled)
cv2.waitKey()
cv2.destroyAllWindows()