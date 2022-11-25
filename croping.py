# Import packages
import cv2
import numpy as np
 


def imagecroper():
    img = cv2.imread('MI.png')
    #print(img.shape) # Print image shape
    #cv2.imshow("original", img)
    
    # Cropping an image

    cropped_image = img[170:1270, 220:1270]
    
    # Display cropped image
    #cv2.imshow("cropped", cropped_image)

    # Save the cropped image
    cv2.imwrite("Cropped Image.jpg", cropped_image)



# cv2.imshow("shortpart", cropped_image)

 
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#imagecroper()