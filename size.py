import cv2
import numpy as np
import PIL
from PIL import Image
import uuid

img = cv2.imread('Cropped Image.jpg')
print(img.shape)
height = img.shape[0]
width = img.shape[1]


print("vertical work start")
# Cut the image in half
width_cutoff = width // 5
second = width_cutoff + width_cutoff
third  = second + width_cutoff
four = third + width_cutoff
five = four + width_cutoff

print(width_cutoff)
print(second)
print(third)
print(four)
print(five)

s1 = img[:, :width_cutoff]
s2 = img[:, width_cutoff:second]
s3 = img[:, second:third]
s4 = img[:, third:four]
s5 = img[:, four:five]

cv2.imwrite("vertical/h1.jpg", s1)
cv2.imwrite("vertical/h2.jpg", s2)
cv2.imwrite("vertical/h3.jpg", s3)
cv2.imwrite("vertical/h4.jpg", s4)
cv2.imwrite("vertical/h5.jpg", s5)


print("vertical work end")
print("----------------------------------------------------------------")


print("horizontal work start")


firstcutimg = cv2.imread('vertical/h1.jpg')
print(firstcutimg.shape)
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


print(height_cutoff)
print(secondfirst)
print(thirdfirst)
print(fourfirst)
print(fivefirst)
print(sixfirst)
print(sevenfirst)
print(eightfirst)
print(ninefirst)
print(tenfirst)
print(elevenfirst)
print(twelvefirst)


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

##crop each frame black line

# def cropframes(path):
#     img1 = cv2.imread(path)
#     cropped_image = img1[15:-12, ::]
#     cv2.imwrite(path, cropped_image)

# for j in namefiles:
#     cropframes(j)




# horizontally concatenates images
# of same height 


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






# posit1 = ["horizontal/h1layer1.jpg","horizontal/h1layer4.jpg","horizontal/h1layer7.jpg","horizontal/h1layer10.jpg"]
# posit2 = ["horizontal/h1layer2.jpg","horizontal/h1layer5.jpg","horizontal/h1layer8.jpg","horizontal/h1layer11.jpg"]
# posit3 = ["horizontal/h1layer3.jpg","horizontal/h1layer6.jpg","horizontal/h1layer9.jpg","horizontal/h1layer12.jpg"]
# finall = [posit1,posit2,posit3]


# for k in range(3):
#     final = [finall[k][0],finall[k][1],finall[k][2],finall[k][3]]
#     imgs = [ Image.open(i) for i in final ]
#     min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]

#     imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
#     imgs_comb = Image.fromarray( imgs_comb)
#     imgs_comb.save( f'final/{k}.png' )

#     img = cv2.imread(f'final/{k}.png')
#     cropped_image = img[::, 10::]
#     cv2.imwrite(f"final/{k}.png",cropped_image)
  










# horizontally concatenates images
# of same height 
# img1 = cv2.imread('final/0.png')
# img2 = cv2.imread('final/1.png')
# img3 = cv2.imread('final/2.png')

# im_h = cv2.hconcat([img1, img2,img3])
# cv2.imwrite("final/man_image.jpeg", im_h)

  
