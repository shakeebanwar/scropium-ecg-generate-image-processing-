import cv2
lead3 = [3,6,9,12]


def preprocess2(arr,nameing):

    for i in range(1,5):
        s_img = cv2.imread(f"horizontal/h1layer{arr[i-1]}.jpg")
        l_img = cv2.imread("testing.jpg")

        if i == 1:
            l_img = cv2.imread("white+still+16-9.001.jpeg")
            x_offset=y_offset=200
            l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

        elif i == 2:
            x_offset=570
            y_offset=160
            l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img


        elif i == 3:
            x_offset=940
            y_offset=150
            l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img


        elif i == 4:
            x_offset=1300
            y_offset=120
            l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
            l_img = l_img[100:350, 200:1750]
    



        cv2.imwrite(f"testing.jpg", l_img)
    
    
    cv2.imwrite(f"leads/{nameing}.png", l_img)





def combine():
    print("combining...")
    img1 = cv2.imread('leads/0.png')
    img2 = cv2.imread('leads/1.png')
    img3 = cv2.imread('leads/2.png')

    im_h = cv2.vconcat([img1, img2,img3])
    cv2.imwrite("leads/finalcomplex.png", im_h)


#preprocess2(lead3,2)
#combine()




























# s_img = cv2.imread("horizontal/h1layer12.jpg")
# l_img = cv2.imread("testing.jpg")


# x_offset=y_offset=200
# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img



# x_offset=570
# y_offset=160
# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img




# x_offset=940
# y_offset=150
# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img


# x_offset=1300
# y_offset=120
# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

# cv2.imshow("result", l_img)

# cv2.imwrite("testing.jpg", l_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


