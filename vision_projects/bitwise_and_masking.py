import cv2
import numpy as np 

#square images
square = np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-2)
cv2.imshow("square",square)
cv2.waitKey(0)

#making ellips
ellipse=np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)

cv2.imshow("ellipse",ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()

#experimenting bitwise operation 
And = cv2.bitwise_and(square,ellipse)
cv2.imshow("biwise and",And)
cv2.waitKey(0)

bitwiseor = cv2.bitwise_or(square,ellipse)
cv2.imshow("bitwise or",bitwiseor)
cv2.waitKey(0)

bitwisexor = cv2.bitwise_xor(square,ellipse)
cv2.imshow("bitwise xor",bitwisexor)
cv2.waitKey(0)

bitwisenot = cv2.bitwise_not(square)
cv2.imshow("bitwise not",bitwisenot)
cv2.waitKey(0)

cv2.destroyAllWindows()