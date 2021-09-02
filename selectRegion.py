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
    l = np.sqrt( (coords[0]-coords[2])**2 + (coords[1]-coords[3])**2 ) 
    print('length:',l)
    a = (coords[2]-coords[0])*(coords[3]-coords[1])
    print('area:',a)
    return coords

