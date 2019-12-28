import cv2
import numpy as np  

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg')
image = cv2.resize(img,(960,540))

height,width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),90,.5)

rotation_img = cv2.warpAffine(image,rotation_matrix,(width,height))
cv2.imshow("roatation image",rotation_img)
cv2.waitKey()
cv2.destroyAllWindows()

#alternate way

rotation_image = cv2.transpose(image)
cv2.imshow("alt rotation image",rotation_image)
cv2.waitKey()
cv2.destroyAllWindows()