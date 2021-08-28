import cv2
import numpy as np

dragging=False

def onMouse(event, x, y, flags, param):
    global dragging
    global img
    global tiled
    global x1, y1, x2, y2
   
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x=%d, y=%d' %(x,y))
        x1=x
        y1=y
        #markedImg = cv2.circle(img, (x,y), radius=3, color=(0, 0, 255), thickness=-1)
        cv2.imshow('img', img)
        dragging=True
    if event == cv2.EVENT_MOUSEMOVE:
        if(dragging==True):
            print('x=%d, y=%d' %(x,y))
            x2=x
            y2=y
            cropped=img[y1:y2, x1:x2]
            tiled = np.tile(cropped,(12,12,1))
            cv2.imshow('tiled', tiled)
    if event == cv2.EVENT_LBUTTONUP:
        #to do: do convolution to find best fit and then tile
        cv2.imwrite('img/tiled.jpg', tiled)
        dragging=False
   
img = cv2.imread("img/JVASP-27851_Positive_20.jpg")

cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()