import cv2
import numpy as np
import PIL
from PIL import Image
import uuid



def complexgenerator():
    print("----------------start-------------------------")
    img = cv2.imread('Cropped Image.jpg')
    height = img.shape[0]
    width = img.shape[1]


    # Cut the image in half
    first = 366

    s1 = img[:, :first]
    cv2.imwrite("vertical/h1.jpg", s1)

    firstcutimg = cv2.imread('vertical/h1.jpg')
    height = firstcutimg.shape[0]
    width = firstcutimg.shape[1]

    # Cut the image in height
    height_cutoff = height // 12
    secondfirst = height_cutoff + height_cutoff
    thirdfirst  = secondfirst  + height_cutoff
    fourfirst = thirdfirst  + height_cutoff
    fivefirst = fourfirst  + height_cutoff
    sixfirst = fivefirst  + height_cutoff
    sevenfirst = sixfirst  + height_cutoff
    eightfirst = sevenfirst  + height_cutoff
    ninefirst = eightfirst  + height_cutoff
    tenfirst = ninefirst  + height_cutoff
    elevenfirst = tenfirst  + height_cutoff
    twelvefirst = elevenfirst  + height_cutoff





    s1 = firstcutimg[:height_cutoff, :]
    s2 = firstcutimg[height_cutoff:secondfirst, :]
    s3 = firstcutimg[secondfirst:thirdfirst, :]
    s4 = firstcutimg[thirdfirst:fourfirst, :]
    s5 = firstcutimg[fourfirst:fivefirst, :]
    s6 = firstcutimg[fivefirst:sixfirst, :]
    s7 = firstcutimg[sixfirst:sevenfirst, :]
    s8 = firstcutimg[sevenfirst:eightfirst, :]
    s9 = firstcutimg[eightfirst:ninefirst, :]
    s10 = firstcutimg[ninefirst:tenfirst, :]
    s11 = firstcutimg[tenfirst:elevenfirst, :]
    s12 = firstcutimg[elevenfirst:twelvefirst, :]

    cv2.imwrite("horizontal/h1layer1.jpg", s1)
    cv2.imwrite("horizontal/h1layer2.jpg", s2)
    cv2.imwrite("horizontal/h1layer3.jpg", s3)
    cv2.imwrite("horizontal/h1layer4.jpg", s4)
    cv2.imwrite("horizontal/h1layer5.jpg", s5)
    cv2.imwrite("horizontal/h1layer6.jpg", s6)
    cv2.imwrite("horizontal/h1layer7.jpg", s7)
    cv2.imwrite("horizontal/h1layer8.jpg", s8)
    cv2.imwrite("horizontal/h1layer9.jpg", s9)
    cv2.imwrite("horizontal/h1layer10.jpg", s10)
    cv2.imwrite("horizontal/h1layer11.jpg", s11)
    cv2.imwrite("horizontal/h1layer12.jpg", s12)


    # namefiles = ["horizontal/h1layer1.jpg","horizontal/h1layer2.jpg","horizontal/h1layer3.jpg","horizontal/h1layer4.jpg","horizontal/h1layer5.jpg","horizontal/h1layer6.jpg","horizontal/h1layer7.jpg","horizontal/h1layer8.jpg","horizontal/h1layer9.jpg","horizontal/h1layer10.jpg","horizontal/h1layer11.jpg","horizontal/h1layer12.jpg"]




    img1 = cv2.imread('horizontal/h1layer1.jpg')
    img2 = cv2.imread('horizontal/h1layer2.jpg')
    img3 = cv2.imread('horizontal/h1layer3.jpg')
    img4 = cv2.imread('horizontal/h1layer4.jpg')
    img5 = cv2.imread('horizontal/h1layer5.jpg')
    img6 = cv2.imread('horizontal/h1layer6.jpg')
    img7 = cv2.imread('horizontal/h1layer7.jpg')
    img8 = cv2.imread('horizontal/h1layer8.jpg')
    img9 = cv2.imread('horizontal/h1layer9.jpg')
    img10 = cv2.imread('horizontal/h1layer10.jpg')
    img11 = cv2.imread('horizontal/h1layer11.jpg')
    img12 = cv2.imread('horizontal/h1layer12.jpg')



    im_h1 = cv2.hconcat([img1, img4,img7,img10])
    im_h2 = cv2.hconcat([img2, img5,img8,img11])
    im_h3 = cv2.hconcat([img3, img6,img9,img12])

    cv2.imwrite("final/0.png", im_h1)
    cv2.imwrite("final/1.png", im_h2)
    cv2.imwrite("final/2.png", im_h3)



    ##vertical concatenates

    img1 = cv2.imread('final/0.png')
    img2 = cv2.imread('final/1.png')
    img3 = cv2.imread('final/2.png')

    im_h = cv2.vconcat([img1, img2,img3])
    cv2.imwrite("final/man_image.jpeg", im_h)


    print("----------------end-------------------------")


#complexgenerator()