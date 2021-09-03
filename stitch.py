import cv2
import numpy as np

def stitch(img, points, n):

    #this is a hack to force same y value for 2 points
    #replace later with fitting
    points[2][1] = points[0][1]
    #find 4th point
    x = points[2][0]+points[1][0]-points[0][0]
    y = points[2][1]+points[1][1]-points[0][1]
    points.append([x,y])


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
    return tiled