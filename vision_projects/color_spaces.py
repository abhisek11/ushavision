
import cv2 
import numpy as np 

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg')
print("image",img)
image = cv2.resize(img,(960,540))
print(image[10,50])
B,G,R = image[10,50]
print(B,G,R)
print(image.shape)

gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(gray_img[10,50])
print(gray_img.shape)

#Another useful color space is HSV Infact HSV is very useful in color filtering.

#H: 0 - 180, S: 0 - 255, V: 0 - 255
hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
H,S,V = cv2.split(hsv_img)
# cv2.imshow('hsv image',hsv_img)
# cv2.imshow('Hue channel', hsv_img[:,:,0])                   #mannually splitting
# cv2.imshow('Saturation channel',hsv_img[:,:,1])
# cv2.imshow('value channel',hsv_img[:,:,2])

cv2.imshow('hsv image',hsv_img)
cv2.imshow('Hue channel',H)
cv2.imshow('Saturation channel',S)
cv2.imshow('value channel',V)

cv2.waitKey()
cv2.destroyAllWindows()

#Let's now explore lookng at individual channels in an RGB image

B,G,R = cv2.split(image)
print(B.shape)
cv2.imshow("Red",R)
cv2.imshow("Green",G)
cv2.imshow("Blue",B)

cv2.waitKey()
cv2.destroyAllWindows()


# Let's re-make the original image,
merged = cv2.merge([B,G,R])
cv2.imshow('Merged image ',merged)

# Let's amplify the blue color
merged = cv2.merge([B+100,G,R])
cv2.imshow('Blue amplified merged image',merged)

cv2.waitKey(0)
cv2.destroyAllWindows()

#color fiilter matrix 

B,G,R = cv2.split(image)
print(image.shape[:2])
print(R.shape)

zeros = np.zeros(image.shape[:2],dtype='uint8')
# print(zeros)
cv2.imshow("RED",cv2.merge([zeros,zeros,R]))
cv2.imshow("GREEN",cv2.merge([zeros,G,zeros]))
cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()
