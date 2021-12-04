import cv2

increment = 1
im_g = cv2.imread("smallgray.png", 0)
for i in im_g.flat:
    print(i)
    i = i + increment
cv2.imwrite("newsmallgray.png", im_g)
