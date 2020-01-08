#Origin_of_Species
import cv2 
import numpy as np  

img = cv2.imread('..\\MasterOpenCV\\images\\Origin_of_Species.jpg',0)
# image = cv2.resize(img,(640,360))
cv2.imshow("original",img)
cv2.waitKey(0)

ret,tresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("ret",ret)
cv2.imshow("THRESH_BINARY",tresh1)
cv2.waitKey(0)

#it is good to use blured image as it remove noises 
image = cv2.GaussianBlur(img,(3,3),0)
#using adaptive threshold
thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow("adaptiveThreshold",thresh)
cv2.waitKey(0)

_,th = cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("OTSU Threshold",th)
cv2.waitKey(0)
#gaussian filter and OTSU threshold
blur = cv2.GaussianBlur(img,(5,5),0)
_,th1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Gaussian OTSU Threshold",th1)
cv2.waitKey(0)


cv2.destroyAllWindows()