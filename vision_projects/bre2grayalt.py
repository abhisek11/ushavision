import cv2

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg',0)
image = cv2.resize(img,(960,540))
cv2.imshow('gray_scale',image)
cv2.waitKey()
cv2.destroyAllWindows()
