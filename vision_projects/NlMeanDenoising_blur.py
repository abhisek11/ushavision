import numpy as np 
import cv2

image = cv2.imread('..\\MasterOpenCV\\images\\elephant.jpg')
cv2.imshow("Original image",image)
cv2.waitKey(0)

#parameters,after None -are ,the filter strength  'h' (5-10 ) is the good range 

#Next is hForColorComponents , set as same values 

dst = cv2.fastNlMeansDenoisingColored(image,None,6,6,7,21)
 
cv2.imshow("fast mean denoising ",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()