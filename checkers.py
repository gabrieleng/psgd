import cv2
import numpy as np

img = np.zeros((1024,1024), np.uint8)
print(img.shape[0]/16)

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        img[i,j] = int(  ( np.floor(i/64)+np.floor(j/64) )%2   * 255)
cv2.imwrite("img/checkers.jpg", img)
