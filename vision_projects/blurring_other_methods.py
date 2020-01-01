import cv2
import numpy as np  

image = cv2.imread('..\\MasterOpenCV\\images\\elephant.jpg')
cv2.imshow("Original image",image)
cv2.waitKey(0)

#averaging done by the conlovuting the image with a normalized box filter 
#takes the pixels under the box and replace the central elements 
#box size need to be odd & positive 

blur  = cv2.blur(image,(3,3))
cv2.imshow("blure image ",blur)
cv2.waitKey(0)

#instead of box filter , gaussian kernal 

gaussian_image = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("Gaussian blurring",gaussian_image)
cv2.waitKey(0)

#takes median of all the pixels under kernal area and central 
#elements is replaced with the median value 
median  = cv2.medianBlur(image,5)
cv2.imshow("median blurring" ,median)
cv2.waitKey(0)

#bilateral is very effective in noise removal area while keeping edges sharp 
bilateral = cv2.bilateralFilter(image,9,75,75)
cv2.imshow("bilateral blurring ",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()