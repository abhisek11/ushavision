import cv2
import numpy as np 

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg')
image = cv2.resize(img,(960,540))
# print("image",image)
height,width = image.shape[:2]

quarter_height,quarter_width = height/4,width/4

T = np.float32([[1,0,quarter_width],[0,1,quarter_height]])
img_translation = cv2.warpAffine(image,T,(width,height))
cv2.imshow('Translation',img_translation)
cv2.waitKey()
cv2.destroyAllWindows()