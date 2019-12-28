import numpy as np 
import cv2

input = cv2.imread('..\\MasterOpenCV\\images\\4star.jpg')
print(input.shape)
print("height of image",input.shape[0],'pixels')
print("width of image",input.shape[1],'pixels')
cv2.imshow('hello world ',input)
cv2.imwrite('output_img.png',input)

cv2.waitKey()
cv2.destroyAllWindows()