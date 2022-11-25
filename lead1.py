import cv2
lead1 = [1,4,7,10]

def preprocess(arr,nameing):

    for i in range(1,5):
       
        s_img = cv2.imread(f"horizontal/h1layer{arr[i-1]}.jpg")
        l_img = cv2.imread("testing.jpg")

        if i == 1:
            l_img = cv2.imread("white+still+16-9.001.jpeg")
            x_offset=y_offset=200
            l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

        elif i == 2:
            x_offset=565
            y_offset=250
            l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img


        elif i == 3:
            x_offset=900
            y_offset=250
            l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img


        elif i == 4:
            x_offset=1250
            y_offset=225
            l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
            
            l_img = l_img[100:350, 200:1750]
    



        cv2.imwrite(f"testing.jpg", l_img)
    
    
    cv2.imwrite(f"leads/{nameing}.png", l_img)
    




#preprocess(lead1,0)

