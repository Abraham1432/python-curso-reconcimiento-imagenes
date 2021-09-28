import cv2

image = cv2.imread('contorno.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
_ , umbral = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

# U need to change image in white and black
contours, hierarchy = cv2.findContours(umbral,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#draw contourns
cv2.drawContours(image,contours,-1,(220, 82, 70),3)

# show images
cv2.imshow('imagen',image)
cv2.imshow('gray',gray)
cv2.imshow('Umbral',umbral)

#0 static / 1 only for video or web cam
cv2.waitKey(0)
cv2.destroyAllWindows()