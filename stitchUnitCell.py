import cv2
import numpy as np

points = []

def findPoint(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONUP:
        points.append([x,y])
        if(len(points)==3):
            #this is a hack to force same y value for 2 points
            #replace later with fitting
            points[2][1] = points[0][1]
            #find 4th point
            x = points[2][0]+points[1][0]-points[0][0]
            y = points[2][1]+points[1][1]-points[0][1]
            points.append([x,y])
            #stitch
            stitch(50)

def findAngle(vector_1, vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)*180/np.pi
    return angle

def stitch(n):
    print(points)
    #find angle between points
    vector_1 = [points[1][0]-points[0][0], points[1][1]-points[0][1]]
    vector_2 = [points[2][0]-points[0][0], points[2][1]-points[0][1]]
    print(findAngle(vector_1,vector_2))

    #crop and tile horizontally
    cropped = img[points[0][1]:points[3][1],points[0][0]:points[2][0]].copy()
    cv2.imshow('crop', cropped)
    tiledX = np.tile(cropped,(1,n))
    cv2.imshow('tiledX', tiledX)

    tiled = tiledX.copy()
    for i in range(1,n):
        xOffset = i*(points[1][0]-points[0][0])
        print(np.shape(tiledX)[0] )

        offset = tiledX[0:np.shape(tiledX)[0], 0:xOffset].copy()
        for y  in range(0,np.shape(offset)[0]):
            for x  in range(0,np.shape(offset)[1]):
                offset[y,x]=0
        tiledXShifted =  np.hstack([offset, tiledX])[0:np.shape(tiledX)[0],0:np.shape(tiledX)[1]]
        tiled = np.vstack([tiled, tiledXShifted])
    
    cv2.imshow('tiled', tiled)
    cv2.imwrite('img/tiled.jpg', tiled)

img = cv2.imread("img/JVASP-27851_Positive_20.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.setMouseCallback('img', findPoint)

print("Click to select origin, a, and b")

cv2.waitKey(0)
cv2.destroyAllWindows()