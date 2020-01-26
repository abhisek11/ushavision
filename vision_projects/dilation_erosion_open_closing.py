import cv2 
import numpy as np 

img = cv2.imread('..\\MasterOpenCV\\images\\opencv_inv.png',0)

cv2.imshow('original',img)
cv2.waitKey(0)

#lets define kernal size 
kernel  = np.ones((5,5), np.uint8)

#errosion & dilations
errosion = cv2.erode(img,kernel,iterations=1)
cv2.imshow("errosion : - ",errosion)
cv2.waitKey(0)

dilations = cv2.dilate(img,kernel,iterations=1)
cv2.imshow("dilation",dilations)
cv2.waitKey(0)

#opening and closing
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("opening",opening)
cv2.waitKey(0)

closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("closing",closing)
cv2.waitKey(0)

cv2.destroyAllWindows()
