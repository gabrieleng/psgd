import cv2
import numpy as np

from selectRegion import selectRegion
from findMatchingRegion import findMatchingRegion
from stitch import stitch

path = "img/"
filename = "JVASP-27851_Positive_20"
extention = ".jpg"

img = cv2.imread(path+filename+extention)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)


o = selectRegion('img') 
a = selectRegion('img')
aFit = findMatchingRegion(img,o,a)
b = selectRegion('img')
bFit = findMatchingRegion(img,o,b)

stiched = stitch(img, [ [o[0],o[1]] , [aFit[0],aFit[1]], [bFit[0],bFit[1]] ] , 40)

cv2.imwrite(path+filename+"_stitched"+extention, stiched)


cv2.waitKey(0)
cv2.destroyAllWindows()