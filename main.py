import cv2
import numpy as np
from prepImg import prepImg
from circleMask import circleMask
from findPeaks import findPeaks
from markedSpots import markedSpots
#import skimage
#load and prepare image
img = cv2.imread("img/test2.png")
pImg = prepImg(img,512)

#circle mask with mean pixel value
r=round(min(pImg.shape)/2)
maskVal = pImg.mean() 
latImg = circleMask(pImg,r,maskVal)

cv2.imshow('latImg', latImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

f=np.fft.fft2(latImg)
f= np.fft.fftshift(f)    
amp=np.abs(f)
amp = 255/np.max(amp)*amp
amp=np.log10(amp) 

cv2.imshow('amp', amp)
cv2.waitKey(0)
cv2.destroyAllWindows()

ampPeaks = findPeaks(amp, .8, 8)
marked = markedSpots(amp, ampPeaks)

cv2.imshow('marked', marked)
cv2.waitKey(0)
cv2.destroyAllWindows()