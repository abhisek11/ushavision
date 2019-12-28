import cv2
import numpy as np 

img = cv2.imread('..\\MasterOpenCV\\images\\IMG_7539.jpg')
image = cv2.resize(img,(960,540))

height,width = image.shape[:2]
start_row,start_col = int(height*.25),int(width*.25)
end_row,end_col = int(height*.75),int(width*.75)

corpped = image[start_row:end_row,start_col:end_col]

cv2.imshow("original",image)
cv2.waitKey()

cv2.imshow("cropped",corpped)
cv2.waitKey()
cv2.destroyAllWindows()