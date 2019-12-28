import cv2 
import numpy as np 

#create a black image 
image = np.zeros((512,512,3),np.uint8)
#can we make trhis in black and white ?
image_bw = np.zeros((512,512),np.uint8)

cv2.imshow('Black rectangle image',image)
cv2.imshow("B&W image ", image_bw)
#lets draw a line over our black square
#draw a diagnol blue line of thickness 5 pxl 
cv2.line(image,(0,0),(511,511),(255,127,0),5)
cv2.imshow("blue line",image)

#lets draw a rectamgle
image_rec = np.zeros((512,512,3),np.uint8)
cv2.rectangle(image_rec,(100,100),(300,250),(127,50,127),5)
cv2.imshow("rectangle ",image_rec)

#lets draw a circle
image_circle = np.zeros((512,512,3),np.uint8)
cv2.circle(image_circle,(350,350),100,(15,75,50),-1)
cv2.imshow("circle",image_circle)

#lets draw a poligons
image_pol = np.zeros((512,512,3),np.uint8)

#lets define four points
pts = np.array([[10,50],[400,50],[90,200],[50,500]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image_pol,[pts],True,(0,0,255),3)
cv2.imshow("polygon",image_pol)

#lets put text in image 

image_text = np.zeros((512,512,3),np.uint8)

cv2.putText(image_text,"My opencv world",(75,290),cv2.FONT_HERSHEY_COMPLEX,1,(100,170,0),2)
cv2.imshow("hello world text",image_text)

cv2.waitKey(0)
cv2.destroyAllWindows()