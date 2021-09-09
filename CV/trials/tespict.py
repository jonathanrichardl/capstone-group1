import cv2

im=cv2.imread("4x6.jpg")
print(im.shape)
cv2.imshow("myself",im)
cv2.waitKey(0)