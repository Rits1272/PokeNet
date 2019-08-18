import cv2
path = './images/300.jpg'

img = cv2.imread(path)
cv2.imshow('image',img)
cv2.waitKey(0)
