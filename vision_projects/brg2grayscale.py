import cv2

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg')
image = cv2.resize(img,(960,540))
cv2.imshow('original',image)
cv2.waitKey()

gray_scale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_scale',gray_scale)
cv2.waitKey()
cv2.destroyAllWindows()

