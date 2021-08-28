import cv2
import numpy as np

dragging=False

def selectFeature(event, x, y, flags, param):
    global dragging
    global img
    global crop
    global x1, y1, x2, y2
    global feature
   
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
            crop = img[0:img.shape[0], 0:img.shape[1]].copy()
            crop = cv2.rectangle(crop, (x1,y1), (x2,y2), (0, 255, 255), 2)
            cv2.imshow('img', crop)
    if event == cv2.EVENT_LBUTTONUP:
        #to do: do convolution to find best fit and then tile
        dragging=False
        feature=img[y1:y2, x1:x2].copy()
        #cv2.imshow("feature", feature)
        print("Feature CHOSEN")
        print("Now draw rectangle with corners at this feature and 3 others ")
        cv2.setMouseCallback('img', selectROI)

def selectROI(event, x, y, flags, param):
    global dragging
    global img
    global roi
    global x3, y3, x4, y4
   
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x=%d, y=%d' %(x,y))
        x3=x
        y3=y
        #markedImg = cv2.circle(img, (x,y), radius=3, color=(0, 0, 255), thickness=-1)
        #cv2.imshow('img', img)
        dragging=True
    if event == cv2.EVENT_MOUSEMOVE:
        if(dragging==True):
            print('x=%d, y=%d' %(x,y))
            x4=x
            y4=y
            roi = crop[0:img.shape[0], 0:img.shape[1]].copy()
            roi = cv2.rectangle(roi, (x3,y3), (x4,y4), (0, 0, 255), 2)
            cv2.imshow('img', roi)
    if event == cv2.EVENT_LBUTTONUP:
        #to do: do convolution to find best fit and then tile
        dragging=False
        print("ROI CHOSEN")
        print("Beginning convolution... ")
        beginConvolution()
        cv2.setMouseCallback('img', unsetCallBack)
def unsetCallBack(event, x, y, flags, param):
    x=1       
def beginConvolution():
    marginX=int(np.round( .2*abs(x2-x1) ))
    marginY=int(np.round( .2*abs(y2-y1) ))

    y5=y1+y4-y3 
    y6=y2+y4-y3 
    x5=x1+x4-x3
    x6=x2+x4-x3

    sumOfDiffs={}
    for i in range (-marginY, marginY):
        for j in range (-marginX, marginX):
            repeatFeature = img[y5+i:y6+i, x5+j:x6+j].copy()
            diff = cv2.subtract(feature,repeatFeature)
            sumOfDiffs[str(i)+','+str(j)]=sum(sum(diff))
            #cv2.imshow("diff", diff)
            #cv2.waitKey(0)

    print(sumOfDiffs)
    minSumOfDiffs=min(sumOfDiffs, key=sumOfDiffs.get)
    print(minSumOfDiffs)
    print(sumOfDiffs[minSumOfDiffs])
    repeatOffsetY = int(minSumOfDiffs.split(',')[0])
    repeatOffsetX = int(minSumOfDiffs.split(',')[1])
    print(repeatOffsetY,repeatOffsetX)
    newROI = img[y3:y4, x3:x4].copy()
    #cv2.imshow("newROI", newROI)

    tiled = np.tile(newROI,(12,24))
    cv2.imshow('tiled', tiled)

img = cv2.imread("img/JVASP-27851_Positive_20.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.setMouseCallback('img', selectFeature)

print("draw rectangle around distinct feature")

cv2.waitKey(0)
cv2.destroyAllWindows()