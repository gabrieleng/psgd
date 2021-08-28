import cv2
import numpy as np

img = cv2.imread("img/JVASP-27851_Positive_20.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blendSize = 10
y1=92
y2=155
x1=204
x2=241
leftBox=img[y1:y2, x1-blendSize:x1]
topBox=img[y1-blendSize:y1, x1:x2]
cropped=img[y1:y2, x1:x2]
rows,cols=leftBox.shape
for i in range(0, rows):
    for j in range(0,cols):
        cropped[i,j+x2-x1-blendSize] = np.round(leftBox[i,j]*j/blendSize) + np.round( cropped[i,j+x2-x1-blendSize] * (blendSize-j)/blendSize)

rows,cols=topBox.shape
for i in range(0, rows):
    for j in range(0,cols):
        cropped[i+y2-y1-blendSize, j] = np.round(topBox[i,j]*i/blendSize) + np.round( cropped[i+y2-y1-blendSize, j] * (blendSize-i)/blendSize)


tiled = np.tile(cropped,(12,22))
cv2.imshow('tiled', tiled)

cv2.waitKey(0)
cv2.destroyAllWindows()

