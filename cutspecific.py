import cv2

img = cv2.imread('Cropped Image.jpg')
#print(img) 
# show the output image
cv2.imshow('orignal', img)




cv2.waitKey(0)
cv2.destroyAllWindows()