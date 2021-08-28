import cv2
import numpy as np

dragging=False




def selectFeature(event, x, y, flags, param):
    global dragging
    global img
    global crop
    global x1, y1, x2, y2
    global feature
    global featureWidth
    global featureHeight
   
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x=%d, y=%d' %(x,y))
        x1=x
        y1=y
        #markedImg = cv2.circle(img, (x,y), radius=3, color=(0, 0, 255), thickness=-1)
        #cv2.imshow('img', img)
        dragging=True
    if event == cv2.EVENT_MOUSEMOVE:
        if(dragging==True):
            print('x=%d, y=%d' %(x,y))
            x2=x
            y2=y
            featureWidth = x2-x1
            featureHeight = y2-y1
            crop = img.copy()
            crop = cv2.rectangle(crop, (x1,y1), (x2,y2), (0, 255, 255), 2)
            cv2.imshow('img', crop)
    if event == cv2.EVENT_LBUTTONUP:
        #to do: do convolution to find best fit and then tile
        dragging=False
        feature=img[y1:y2, x1:x2].copy()
        #cv2.imshow("feature", feature)
        print("Feature CHOSEN")
        print("Now find a ")
        cv2.setMouseCallback('img', findA)

def findA(event, x, y, flags, param):
    global ax
    global ay
    if event == cv2.EVENT_MOUSEMOVE:
        print('x=%d, y=%d' %(x,y))
        print('a')
        imgOverlay = img.copy()
        imgOverlay = cv2.rectangle(imgOverlay, (x1,y1), (x2,y2), (0, 255, 255), 2)
        imgOverlay[y:y+y2-y1, x:x+x2-x1] = img[y1:y2, x1:x2]
        cv2.imshow('img', imgOverlay)
    if event == cv2.EVENT_LBUTTONUP:
        ax=x
        ay=y
        cv2.setMouseCallback('img', findB)
def findB(event, x, y, flags, param):
    global bx
    global by
    if event == cv2.EVENT_MOUSEMOVE:
        print('x=%d, y=%d' %(x,y))
        print('b')
        imgOverlay = img.copy()
        imgOverlay = cv2.rectangle(imgOverlay, (x1,y1), (x2,y2), (0, 255, 255), 2)
        imgOverlay[y:y+y2-y1, x:x+x2-x1] = img[y1:y2, x1:x2]
        cv2.imshow('img', imgOverlay)
    if event == cv2.EVENT_LBUTTONUP:
        bx=x
        by=y
        print(ax,ay,bx,by)

img = cv2.imread("img/JVASP-27851_Positive_20.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.setMouseCallback('img', selectFeature)

print("draw rectangle around distinct feature")

cv2.waitKey(0)
cv2.destroyAllWindows()