import numpy as np
import cv2

def selectRegion(window):
    coords=[]
    def callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print('x=%d, y=%d' %(x,y))
            coords.append(x)
            coords.append(y)
        if event == cv2.EVENT_MOUSEMOVE:
            print('x=%d, y=%d' %(x,y))
        if event == cv2.EVENT_LBUTTONUP:
            print('x=%d, y=%d' %(x,y))
            coords.append(x)
            coords.append(y)
            cv2.setMouseCallback(window, lambda *args : None)  
    print("Please select region...")
    test=cv2.setMouseCallback('img', callback)
    while len(coords)<4:   
        cv2.waitKey(1)
    return coords

def measureLength(window):
    r = selectRegion('img')
    print(r)
    l = np.sqrt( (r[0]-r[2])**2 + (r[1]-r[3])**2 ) 
    print(l)

img = cv2.imread("img/JVASP-27851_Positive_20.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', img)

measureLength('img')



cv2.waitKey(0)
cv2.destroyAllWindows()