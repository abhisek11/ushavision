import cv2 
import numpy as np  

img = cv2.imread('..\\MasterOpenCV\\images\\gradient.jpg',0)
# image = cv2.resize(img,(640,360))
cv2.imshow("original",img)
# cv2.waitKey(0)

ret,tresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("ret",ret)
cv2.imshow("THRESH_BINARY",tresh1)

ret,tresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
print("ret",ret)
cv2.imshow("THRESH_BINARY_INV",tresh2)

ret,tresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
print("ret",ret)
cv2.imshow("THRESH_TRUNC",tresh3)

ret,tresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
print("ret",ret)
cv2.imshow("THRESH_TOZERO",tresh4)

ret,tresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
print("ret",ret)
cv2.imshow("THRESH_TOZERO_INV",tresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()